from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return open("app.html").read()

@app.route('/<filename>')
def temp(filename):
    return send_file(filename)

if __name__ == '__main__':
    app.run(port=1851)