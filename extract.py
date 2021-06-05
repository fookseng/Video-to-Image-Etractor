# Importing all necessary libraries
import cv2
import os
import time
from skimage.filters import threshold_triangle
import matplotlib.pyplot as plt
import numpy as np

def frame_capture(file, counter, number, frame_no, auto):
  # Playing video from file:
  file = '.'+file
  cap = cv2.VideoCapture(file)
  extract_dir = 'extracted_data'
  try:
      if not os.path.exists(extract_dir):
          os.makedirs(extract_dir)
  except OSError:
      print('Error: Creating directory of data')

  currentframe = counter
  num = number

  while(True):
      # Capture frame by frame
      ret, frame = cap.read()
      if ret:
          # if video is still left continue creating images
          name = './'+extract_dir+'/' + str(num) + '_' + str(currentframe)
          file_name = './'+extract_dir+'/' +str(num) + '_' + str(currentframe) + '.jpg'
          if cap.get(cv2.CAP_PROP_POS_FRAMES) % frame_no == 0:
              if auto:
                  print('Creating...' + file_name)
                  cv2.imwrite(file_name, frame)
                  currentframe += 1
              else:
                  image = frame
                  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                  frame_new = image
                  image = cv2.convertScaleAbs(image, alpha=1, beta=50)
                  value = threshold_triangle(image)
                  ret, edged = cv2.threshold(image, value, 255, cv2.THRESH_TRIANGLE)
                  edged = cv2.GaussianBlur(edged, (5, 5), 10.0)
                  edged = cv2.Canny(edged, 40, 100)
                  edged = cv2.dilate(edged, None, iterations=1)
                  edged = cv2.erode(edged, None, iterations=1)
                  name_edged = name + 'edged' + '.jpg'
    
                  numpy_horizontal = np.hstack((frame_new, edged))
                  cv2.namedWindow('Comparison', cv2.WINDOW_NORMAL)
                  cv2.resizeWindow('Comparison', 1800, 1200)
                  cv2.imshow('Comparison', numpy_horizontal)
    
                  key = cv2.waitKey(0)
                  if key == ord('q'):
                      cv2.destroyAllWindows()
                  elif key == ord('s'):
                      print('Creating...' + file_name)
                      cv2.imwrite(file_name, frame)
                      #cv2.imwrite(name_edged, edged)
                      currentframe += 1
                  elif key == ord('e'):
                      break 
                  else:
                      cv2.destroyAllWindows()
          else:
              currentframe = currentframe
      else:
          break

  cap.release()
  cv2.destroyAllWindows()


if __name__ == '__main__':
    counter = 0
    number = 1
    frame = 15
    source_dir = 'videos'
    
    for file in os.listdir("./"+source_dir):
        if file.endswith(".mp4"):
            path=os.path.join("/"+source_dir, file)
            frame_capture(path, counter, number, frame, 1)
            print(path)
        number = number + 1


