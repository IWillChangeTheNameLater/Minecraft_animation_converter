import os

import cv2
import numpy as np


while True:
    file = input('Enter the path to the file: ')
    if os.path.exists(file): break
while True:
    frame_reduction = int(input('Enter how many times you want to reduce the number of frames: '))
    if frame_reduction > 0: break
while True:
    video_reduction = int(input('Enter how many times you want to reduce the video resolution (even number): '))
    if video_reduction > 0: break

video = cv2.VideoCapture(file)
width, height = int(video.get(4)), int(video.get(3))
smallest_side = min(width, height)
final_resolution = smallest_side // video_reduction
side = 1
while side * 2 <= final_resolution: side *= 2

# Make the initial frame
frame = video.read()[1]
canvas = cv2.resize(frame[(width - smallest_side) // 2 : (width - smallest_side) // 2 + smallest_side, 
                   (height - smallest_side) // 2 : (height - smallest_side) // 2 + smallest_side], 
                    (side, side))

# Add frame to canvas
count = frame_reduction
while video.isOpened():
    ret, frame = video.read()
    if not ret: break
    if count == frame_reduction:
        count = 0
        frame = cv2.resize(frame[(width - smallest_side) // 2 : (width - smallest_side) // 2 + smallest_side, (height - smallest_side) // 2 : (height - smallest_side) // 2 + smallest_side], 
                           (side, side))
        canvas = np.concatenate((canvas, frame))
    count += 1

# Make files
full_name = '.'.join(file.split('.')[0:-1])
cv2.imwrite(full_name + '.png', canvas)
mcmeta = open(full_name + '.png.mcmeta', 'w')
mcmeta.write(
'''{
    "animation": {
        "frametime": ''' + str(20 / video.get(cv2.CAP_PROP_FPS)) + '''
    }
}''')
mcmeta.close()
