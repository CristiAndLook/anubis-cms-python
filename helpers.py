import os
import platform

def clean_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def read_text(long_min=0, long_max=100, msg=None):
    if msg:
        print(msg)

    while True:
        text = input("> ")

        if len(text) > long_min or len(text) <= long_max:
            print(f"Error: La longitud del texto debe estar entre {long_min} y {long_max}")
            return text