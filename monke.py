import keyboard
import time
import json
from tkinter import messagebox
inp = input("write a json file name:")

def write_sentence():
    # Read sentences from JSON file
    
    with open(inp, 'r') as f:
        sentences = json.load(f)

    # Iterate over each sentence and write it
    for sentence in sentences:
        keyboard.write(sentence)
        keyboard.press_and_release('enter')
        time.sleep(1)

def on_key_press(event):
    if event.event_type == keyboard.KEY_DOWN:
        write_sentence()

# Replace "insert" with the key you want to trigger the sentence writing
keyboard.on_press_key("insert", on_key_press)

print("Listening for key 'insert' press. Press Ctrl+C to exit.")
keyboard.wait("ctrl+c")  # Wait for Ctrl+C to exit
