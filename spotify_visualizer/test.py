from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=None)


@app.get("/")
def index():
    return send_from_directory(app.root_path, "app.html")

@app.get("/<filename>")
def file(filename):
    return send_from_directory(app.root_path, filename)

if __name__ == "__main__":
    app.run(port=5173)
