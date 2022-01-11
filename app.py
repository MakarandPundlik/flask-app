from flask import Flask

app = Flask(__name__)#reserved keywords 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"