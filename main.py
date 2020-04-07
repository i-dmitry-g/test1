from flask import Flask

app = Flask(__name__)

@app.route("/index")
def index():
    return "Привет от приложения Flask"


if __name__ == '__main__':
    app.run()
