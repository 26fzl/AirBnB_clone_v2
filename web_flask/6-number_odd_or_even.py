#!/usr/bin/python3
'''starts a Flask web application'''

from flask import Flask, render_template as templates

exu = Flask(__name__)


@exu.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def Odd_even(n):
    if n % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    return templates('6-number_odd_or_even.html', n=n, even_odd=even_odd)


if __name__ == '__main__':
    exu.run(host='0.0.0.0', port='5000')
