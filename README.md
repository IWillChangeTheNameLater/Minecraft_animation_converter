# Minecraft_animation_converter

The application which converts videos to Minecraft animated textures format.

## Installation

1. Clone this repository to your computer using
   `https://github.com/IWillChangeTheNameLater/Minecraft_animation_converter.git`
2. Install the required packages by running the following command:
   `pip install -r requirements.txt`
3. Run the `main.py` script to start using the program.

## Usage

To use this application, follow these steps:

1. Open the command prompt or terminal on your computer.
2. Navigate to the directory where you cloned the repository using `cd <path_to_repository>`
3. Run the following command to start the application: `python main.py`
4. Follow the instructions in the command prompt/terminal to enter the path to the video file, resolution of the output
   animation frame, and how many times you want to reduce the number of frames of the animation.
5. After the conversion is complete, the output files will be saved in the same directory as the source video file.

## Example

By running the program, specifying the name of the video file and
leaving the other parameters by default,
we get the texture image and the .mcmeta file
in the source video directory.

The video (gif, in our case):

![example.gif](example.gif)

The output texture image:
[exapmle.png](example.png)

The output .mcmeta file with the animation properties:
[example.png.mcmeta](example.png.mcmeta)

