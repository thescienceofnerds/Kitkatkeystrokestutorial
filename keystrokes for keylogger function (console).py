#      Code for my guy kitkat #

# all the imports are here
from pynput.keyboard import Key, Listener # pip installpynput, pip install Listener

def on_press(key):       # defines that when a key is pressed...
    print(key)    # ... It prints the name of that key in the console

with Listener(on_press=on_press) as listener: # uses listener to record a keypress, whenever a key is pressed
    listener.join() # tells the listener to listen
