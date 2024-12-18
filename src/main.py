import os

from util.detector import detect_duplicates

def load_data() -> str:
    with open('../data/references.bib', 'r') as file:
        data = file.read()
    return data

if __name__ == '__main__':
    data: str = load_data()

    duplicates = detect_duplicates(data)