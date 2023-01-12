import glob
import os
import shutil
from PIL import Image, ImageOps, ImageEnhance, ImageDraw, ImageFont


class Editor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.img = Image.open(filepath).convert("RGBA")

    def change_contrast(self, amount=1.5):
        enhancer = ImageEnhance.Contrast(self.img)
        self.img = enhancer.enhance(1.5)

    def grayscale(self):
        self.img = ImageOps.grayscale(self.img)
        self.img = self.img.convert("RGBA")

    def invert_horizontal(self):
        print("rotated image")
        self.img = self.img.rotate(180)

    def make_thumbnail(self, size=(128, 128)):
        self.img.thumbnail(size)

    def square_image(self, size=200):
        print("Make square")

        (w, h) = self.img.size

        if w > h:
            x = (w - h) * 0.5
            y = 0
            box = (x, y, h + x, h + y)
        else:
            x = 0
            y = (h - w) * 0.5
            box = (x, y, x + w, y + w)

        self.img = self.img.resize((size, size), box=box)

    def write_on_image(self):
        font = ImageFont.truetype("ibm-plex-mono.ttf", 24)
        drawer = ImageDraw.Draw(self.img)

        drawer.multiline_text(
            (32, 32),
            "writing\non\nhere",
            font=font,
            fill=(255, 0, 0, 100))

    def save(self, output_filepath):
        print("Your image was saved!")

        if self.filepath.endswith(".jpg"):
            self.img = self.img.convert("RGB")

        self.img.save(output_filepath)


inputs = glob.glob("inputs/*.jpg")

os.makedirs("results", exist_ok=True)

for filepath in inputs:
    output = filepath.replace("inputs", "results")
    image = Editor(filepath)
#    image.change_contrast()
#    image.grayscale()
#    image.invert_horizontal()
#    image.make_thumbnail((300, 300))
#    image.square_image()
#    image.write_on_image()
    image.make_ascii()
    image.save(output)
