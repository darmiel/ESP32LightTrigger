from PIL import Image

IN_FILE: str = "camera.png"
COLOR: int = 1

image: Image = Image.open(IN_FILE)
pix = image.load()

for y in range(image.size[1]):
    for x in range(image.size[0]):
        val = pix[x, y]
        if val[3] != 0:
            print(f"display.pixel(x + {x}, y + {y}, {COLOR})")