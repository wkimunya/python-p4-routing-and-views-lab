#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(param+1))  
    response_text = f'Counting numbers:\n{numbers}\n\n'  
    return Response(response_text, content_type='text/plain')

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
