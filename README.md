# Image-Etractor
Extract image from video(.mp4) and save in .jpg format.

## Step 1:
Store all the videos(.mp4) in a folder named "videos" in the same directory with the .py file.
## Step 2:
Run the python script. 
## Step 3:
### auto mode (auto = 1 by default)
Extract image automatically without pressing any key. 
### manual mode (auto = 0)
Press any key to skip to next frame.
Press 'e' to skip to next video.
Press 's' to save the current frame.
## Step 4:
Images will be saved in a folder named 'extracted_data' in the same directory.

## Arguments
In the main function, you can adjust the value for the following variable to suit your requirements:
- frame: (default is 15), the interval of number of frame. For example, if your video has a total of 60 frames, we will only extract frame15, frame30, frame45 and frame60. 
- auto: (default is 1), Automatically extract all the videos to images. If auto = 0, you can preview each frame and decide whether to extract or not.

