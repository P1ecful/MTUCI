import os

def getPWD() -> str:
    return f'Директория: {os.path.dirname(os.path.abspath(__file__))}'

