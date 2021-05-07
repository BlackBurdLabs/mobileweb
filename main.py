from flask import Flask
app = Flask(__name__)

@app.route('/')
def hell_world():
    return 'Hello World'

@app.route('/login')
def login():
    return 'login'


    
if __name__ == '__main__':
    app.run()