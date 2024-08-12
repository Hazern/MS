from pathlib import Path
import os
from tkinter import Tk, Label
from PIL import Image, ImageTk

image_count = []
mod_path = Path(__file__).parent / "Mod_Sorter_by_SwimSuit_Rarity"

for Class_image_folder in mod_path.iterdir():
    for mod_folder in Class_image_folder.iterdir():
        for image in mod_folder.glob("*.jpg"):
            image_count.append(str(image))
print(len(image_count))