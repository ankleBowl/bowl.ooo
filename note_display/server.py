from flask import Flask
from PIL import Image

app = Flask(__name__)

image_data = b"\xff" * int(((300 * 400) / 8))

@app.route("/")
def hello_world():
    return image_data

def read_image():
    img = Image.open("display_image.png")
    img = img.resize((300, 400))
    img = img.convert("1")
    img = Image.eval(img, lambda x: 255 - x)

    return img.tobytes()

image_data = read_image()

if __name__ == "__main__":
    app.run(host="10.0.0.83", port=5002)