# Minecraft_animation_converter

The application which converts videos to Minecraft animated textures format.

## Installation

1. Clone this repository to your computer using

   `git clone https://github.com/IWillChangeTheNameLater/Minecraft_animation_converter.git`
   
2. Install the required packages by running the following command:
   
   `python -m pip install -r requirements.txt`
   
3. Run the `main.py` file to start using the program with:
   
   `python main.py`

## Usage

To use this application, follow these steps:

1. Open the command prompt or terminal on your computer.
2. Navigate to the directory where you cloned the repository using: 
   `cd Minecraft_animation_converter`
   
4. Run the following command to start the application: 
   `python main.py`
   
6. Follow the instructions in the command prompt/terminal to enter the path to the video file, resolution of the output
   animation frame, and how many times you want to reduce the number of frames of the animation.
5. After the conversion is complete, the output files will be saved in the same directory as the source video file.

### Or

Just run the `Minecraft_animation_converter.exe` executable file.

## Example

By running the program, specifying the name of the video file and
leaving the other parameters by default,
we get the texture image and the .mcmeta file
in the source video directory.

The input video file (gif, in our case):

![example.gif](example.gif)

The output texture image:
[example.png](example.png)

The output .mcmeta file with the animation properties:
[example.png.mcmeta](example.png.mcmeta)

