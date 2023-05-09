import os
from math import log2
from pathlib import Path

import cv2
import numpy as np


def get_source_path():
    request_phrase = 'Enter the path to the source video file: \n'

    while True:
        source_path = input(request_phrase)

        if not source_path:
            print('The path is empty!')
            continue

        source_path = Path(source_path)

        if not source_path.exists():
            print('The path does not exist!')
            continue

        return source_path


def get_animation_resolution():
    request_phrase = 'Enter the resolution of the output animation frame. \n' \
                     'It must be equal to 2^n: \n'

    while True:
        video_resolution = input(request_phrase)

        if not video_resolution.isdigit():
            print('The resolution must be a number!')
            continue

        video_resolution = float(video_resolution)

        if not video_resolution.is_integer():
            print('The resolution must be an integer!')
            continue

        video_resolution = int(video_resolution)

        if video_resolution <= 0:
            print('The video resolution must be bigger than 0!')
            continue
        elif not (log2(video_resolution)).is_integer():
            print('The video resolution must be a power of 2!')
            continue

        return video_resolution


def get_frames_count_reduction():
    request_phrase = 'Enter how many times do you want to reduce the ' \
                     'number of frames of the animation: \n'

    while True:
        frame_reduction = input(request_phrase)

        if not frame_reduction.isdigit():
            print('The input must be a number!')
            continue

        frame_reduction = float(frame_reduction)

        if not frame_reduction.is_integer():
            print('The input must be an integer!')
            continue

        frame_reduction = int(frame_reduction)

        if frame_reduction <= 0:
            print('The input must be bigger than 0!')
            continue

        return frame_reduction


def reduce_to_power_of_2(num):
    return 2 ** int(log2(num))


def crop_rectangle_as_square(frame):
    width, height, _ = frame.shape

    side_size = min(width, height)

    start_width = (width - side_size) // 2
    end_width = start_width + side_size
    start_height = (height - side_size) // 2
    end_height = start_height + side_size
    frame = frame[start_width:end_width, start_height:end_height]

    return frame


def resize_frame(frame, resize_size):
    frame = cv2.resize(frame, (resize_size, resize_size))
    return frame


def convert_video_to_animation_img(video, resize_size=None, each_frame_numbered=1):
    img = None

    frame_i = 0
    while True:
        ret, frame = video.read()

        if not ret: break

        if frame_i % each_frame_numbered == 0:
            frame = crop_rectangle_as_square(frame)
            if resize_size:
                frame = resize_frame(frame, resize_size)

            if img is None:
                img = frame
            else:
                img = np.concatenate((img, frame))

        frame_i += 1

    return img


def save_animation_img(img, name):
    cv2.imwrite(name + '.png', img)


def save_animation_properties(frametime, name):
    properties_text = '''{
		"animation": {
			"frametime": ''' + str(frametime) + ''' 
	}
}'''

    with open(name + '.png.mcmeta', 'w') as mcmeta:
        mcmeta.write(properties_text)


def save_minecraft_animation(img, fps, name='minecraft_animation'):
    name = os.path.splitext(name)[0]

    save_animation_img(img, name)
    save_animation_properties(20 / fps, name)


def main():
    source_path = get_source_path()
    animation_resolution = get_animation_resolution()
    frames_count_reduction = get_frames_count_reduction()
    video = cv2.VideoCapture(str(source_path))

    animation_img = convert_video_to_animation_img(
        video,
        animation_resolution,
        frames_count_reduction)

    save_minecraft_animation(
        animation_img,
        video.get(cv2.CAP_PROP_FPS) / frames_count_reduction,
        source_path.name)


if __name__ == '__main__':
    main()
