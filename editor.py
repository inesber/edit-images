import glob
import os
import shutil
from PIL import Image


class Editor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.img = Image.open(filepath)

    def invert_horizontal(self):
        print("rotated image")
        self.img = self.img.rotate(180)

    def make_thumbnail(self):
        size = 128, 128
        self.img.thumbnail(size)

    def save(self, output_filepath):
        print("Your image was saved!")
        self.img.save(output_filepath)


inputs = glob.glob("inputs/*.jpg")

os.makedirs("results", exist_ok=True)

for filepath in inputs:
    output = filepath.replace("inputs", "results")
    image = Editor(filepath)
    image.invert_horizontal()
    image.make_thumbnail()
    image.save(output)
