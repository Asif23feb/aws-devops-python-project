from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! my name is Asif Hoda'

if __name__ == '__main__':
    app.run()

