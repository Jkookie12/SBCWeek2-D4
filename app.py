from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Activity 1 - Home Page</h1>"

@app.route('/about')
def about():
    return "<h2>This is the About page for Activity 2</h2>"


if __name__ == '__main__':
    app.run(debug=True)

