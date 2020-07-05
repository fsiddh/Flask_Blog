from flask import Flask

# Instantiates flask app
app = Flask(__name__)


# 'routes' are what we write on browser to go on different pages
# '/' and '/home' takes us at same location where home() is loaded
@app.route("/")
@app.route("/home")
def home():
    return '<h1>Hello World</h1>'


# When you search 'http://127.0.0.1:5000/about' in browser your about function loads
@app.route("/about")
def about():
    return 'Hello, my name is Falansh Siddh'


if __name__ == '__main__':
    app.run(debug=True)