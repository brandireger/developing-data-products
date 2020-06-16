from flask import Flask
from flask import render_template
from flask import request
from random import randint
from model import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll-dice')
def rolldice():
    return render_template(\
        'roll-dice.html', \
        dice_roll1 = randint(1, 6), \
        dice_roll2 = randint(1, 6), \
        dice_roll3 = randint(1, 6))

@app.route('/my-first-form')
def my_first_form():
    return render_template('my-first-form.html')

@app.route('/make-greeting', methods=['POST'])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template('greeting-result.html', greeting=greeting)

@app.route('/spam-or-ham')
def spam_form():
    return render_template('spam-form.html')

@app.route('/spam-ham-result', methods=['POST'])
def spam_ham_prediction():
    message = request.form['message']
    result = predict(message)
    return render_template('spam-ham-result.html', message=message, result=result)