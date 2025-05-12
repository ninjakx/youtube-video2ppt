# youtube-video2ppt

[![Hits](https://hitscounter.dev/api/hit?url=https%3A%2F%2Fgithub.com%2Fninjakx%2Fyoutube-video2ppt&label=Count&icon=github&color=%23198754)](https://hits.seeyoufarm.com)

**Note:** For videos more than 15 min of length you might have more than 200 slides in ppt so some Manual deletion might require :( as per your convenience.

This is a command utility to create ppt from the youtube educational video. 
Initally designed for youtube channel: `StatQuest with Josh Starmer` :heart: 
I find his works amazing and I wanted to get the slides out from the video so that I can make a note for revision so I decided to write this script using openCV and shell scripting. 
but now expanded to other usecases to capture the slides from the lecture.

**Note:** It's still having a bug if selected regions are overlapped then overlapped area is shown as white bg in the ppt slides. Need to fix this issue.



## Install
### Via compiling from source:
```console
$ git clone git@github.com:ninjakx/youtube-video2ppt.git
$ cd youtube-video2ppt
```

## Usage
Install all the necessary packages by:

`pip install -r requirements.txt`

then run `bash vid2ppt.sh`

### Demo:

**Initial version:**
![](https://github.com/ninjakx/youtube-video2ppt/blob/main/out1.png)

**Newer:**

demo: 

![](https://github.com/ninjakx/youtube-video2ppt/blob/main/vid2ppt-demo.gif)

### Result:

![](https://github.com/ninjakx/youtube-video2ppt/blob/ebaf74d3c55192b1c4a832d147fe9fea08fa098b/output.png)
<img width="1197" alt="image" src="https://github.com/ninjakx/youtube-video2ppt/assets/29797787/957d8eef-f6a0-4ad8-a7b0-3dcd6bbc66d1">


## TO DO:

- [ ] Use Deep Learning based solution to filter out the frames containing only headers.
- [ ] Automate it to create word doc with image and transcribe audio text below the image (will try to introduce text summarizer).
- [ ] Make it to work on black screen teaching method.
- [ ] Using detection model, mask the person to capture only the board and its content to create ppt using Computer Vision.


Feel free to contribute.

## Please consider giving :star: if you like it. 😊

