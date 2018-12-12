"""Script to run chat_generator portion of my Mad Libs project.
The chat_generator is my main function that enables users to input username and password of their own choice to begin the game of Mad Libs. The function checks if the length of string username is within the boundaries of 5 to 10 character limit, and checks if the previously encrypted password matches with the copied password based on user's input. The function will finally call the mad_libs() function to play the Mad Libs game, and allow the user to replay the game by calling the replay_game() function. 
"""


# This adds the directory above to our Python path so that we can add import my custom python module
# code into this script
import sys
sys.path.append('../')


# Imports
from my_module.functions import chat_generator


# PYTHON SCRIPT HERE which is my main function chat_generator()
chat_generator()
