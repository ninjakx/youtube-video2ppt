import pytube
from pathlib import Path
import argparse
import cv2
import numpy as np
from img2ppt import create_ppt

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--start", required=False, type=int, default=0,	help="Start of the video")
ap.add_argument("-p", "--path", required=False, default='', help="Path to save slides")
args = vars(ap.parse_args())

#print(Path(args['path']).glob('*.mp4'))
vid_path = next(Path(args['path']).glob('*.mp4'))
#print(vid_path)
vidcap = cv2.VideoCapture(f"{vid_path}")
success,image = vidcap.read()
#print(image.shape)
dir_path = args['path']
#################### Setting up parameters ################

seconds = 1
fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
multiplier = fps * seconds

#print(multiplier)
#################### Initiate Process ################
count = 0
threshold = 0.002
while success:
    frameId = int(round(vidcap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
    success, image = vidcap.read()
    if count==0:
        previous = image
        # cv2.imwrite(f"{vid_path}/frame{frameId}.jpg", image)
    count =+ 1
    
    if frameId % int(multiplier) == 0 and frameId > int(multiplier)*args['start']:
        current = image
                
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
            cv2.imwrite(f"{dir_path}/frame{frameId}.jpg", image)
        
        previous = current

vidcap.release()
create_ppt(dir_path)
print("Complete")





