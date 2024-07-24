#In this project i need to organize the files within a folder according its 
#file type, example: mp3, mp4, .py, .png


import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'], 
    "AUDIOS": ['.m4a', '.m4b', '.mp3'], 
    "VIDEOS": ['.mov', '.avi', '.mp4'], 
    "IMAGES": ['.jpg', '.jpeg', '.png']
}

def pickDictionary(value):
    for category, suffixes in SUBDIRECTORIES.items():
        if value in suffixes:
            return category
    return 'MISC'


#print(pickDictionary('.pdf'))

def organizeDirectory():
    for i in os.scandir():
        if i.is_dir():
            continue
        filePath = Path(i)
        fileType = filePath.suffix.lower()
        directory = pickDictionary(fileType)
        directoryPath = Path(directory)
        if directoryPath.is_dir()  != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))
    print(fileType)

organizeDirectory()










