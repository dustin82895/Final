
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/wallet')
def wallet():
    return render_template('wallet.html')

@app.route('/bots')
def bots():
    return render_template('bots.html')

@app.route('/casino')
def casino():
    return render_template('casino.html')

@app.route('/drop')
def drop():
    return render_template('drop.html')

if __name__ == '__main__':
    app.run(debug=True)
