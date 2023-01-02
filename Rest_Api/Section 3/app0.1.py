from flask import Flask

app = Flask(__name__)

@app.route('/') #endpoint '/'-> is basically home page
def home():
    return "hello, world!"

app.run(port=5000) #127.0.0.1.5000