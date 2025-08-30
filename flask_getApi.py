# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World Jay !"
@app.route("/jay")
def h_jau():
    return "This is  Jay !"
if __name__ == '__main__':
    app.run(port=5000, debug=True)