import os

def clear_screen():
    return os.system('cls' if os.name == 'nt' else 'clear')