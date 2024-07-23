from flask import Flask, render_template, request
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    password = request.form['password']
    timeframe = int(request.form['timeframe'])
    gpu = request.form['gpu']
    electricity = float(request.form['electricity'])

    # Implement the cost calculation logic here
    # ...

    return render_template('result.html', cost=cost)