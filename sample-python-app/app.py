from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! My name is Asif Hoda.i am devops enthusiast'

if __name__ == '__main__':
    app.run()

