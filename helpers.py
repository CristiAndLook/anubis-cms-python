import os
import platform

def clean_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def read_text(long_min=0, long_max=100, msg=None):
    if msg:
        print(msg)

    while True:
        text = input("> ")

        if len(text) >= long_min and len(text) <= long_max:
            return text
        else:
            print(f"Error: La longitud del texto debe estar entre {long_min} caracteres y {long_max} caracteres")