import pytube
from pathlib import Path
import argparse
import cv2
import numpy as np
from img2ppt import create_ppt
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--start", required=False, type=int, default=0,	help="Start of the video")
ap.add_argument("-p", "--path", required=False, default='', help="Path to save slides")
ap.add_argument("-f", "--flag", required=False, default='', help="Mask the area(to ignore) using selection tool for checking the difference")
args = vars(ap.parse_args())

#print(Path(args['path']).glob('*.mp4'))
vid_path = next(Path(args['path']).glob('*.mp4'))
vidcap = cv2.VideoCapture(f"{vid_path}")
success,image = vidcap.read()
dir_path = args['path']

#################### Setting up parameters ################

seconds = 1 #4 -> if there is scrolling (this is the best we can do to get from the moving scrollable contents like arpit bhayani's videos)
fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
multiplier = fps * seconds

#################### Initiate Process ################
count = 0
threshold = 0.002
fl = (args['flag']=='y')

while success:
    frameId = int(round(vidcap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
    success, image = vidcap.read()
    if frameId <= int(multiplier)*args['start']:
        continue
    if count==0:
        previous = image
        # Mask the area to ignore (because we are checking the changes between two frames), 
        # we don't want to include the area like human in window because it's gonna introduce the changes.
        if (fl):
            windowName = "select the area"
            global coords, orig_imgs, nu
            orig_imgs = []
            coords = []
            rvs = cv2.selectROIs(windowName=windowName,img=image)
            nu = len(rvs)
            for i in range(nu): 
                r = rvs[i]
                coords.append([int(r[1]),int(r[1]+r[3]),int(r[0]),int(r[0]+r[2])])
                orig_img = image[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])].copy()
                orig_imgs.append(orig_img)
                image[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])] = (255, 255, 255)
    count =+ 1
    
    if frameId % int(multiplier) == 0:
        if fl and image is not None:
            orig_imgs = []
            for i in range(nu): 
                coord = coords[i].copy()
                orig_img = image[coord[0]:coord[1], coord[2]:coord[3]].copy()
                orig_imgs.append(orig_img)
                image[coord[0]:coord[1], coord[2]:coord[3]] = (255, 255, 255)
            
        current = image

        try:

            prev = cv2.cvtColor(previous, cv2.COLOR_BGR2GRAY)
            cur = cv2.cvtColor(current, cv2.COLOR_BGR2GRAY)

            (thresh, im_bw_prev) = cv2.threshold(prev, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            (thresh, im_bw_cur) = cv2.threshold(cur, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

            # Set up and feed background subtractor (cf. tutorial linked in question)
            backSub = cv2.createBackgroundSubtractorMOG2()
            _ = backSub.apply(im_bw_prev)
            mask = backSub.apply(im_bw_cur)
            n_white_pix = np.sum(mask == 255)/mask.size
            if n_white_pix > threshold:
                image1 = image.copy()
                if fl:
                    for i in range(nu): 
                     coord = coords[i].copy()
                     image1[coord[0]:coord[1], coord[2]:coord[3]] = orig_imgs[i].copy()
                cv2.imwrite(f"{dir_path}/frame{frameId}.jpg", image1)
            
            previous = current.copy()
        except:
            continue

vidcap.release()
create_ppt(dir_path)
print("Complete")





