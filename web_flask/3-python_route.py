#!/usr/bin/python3
'''starts a Flask web application'''

from flask import Flask

exu = Flask(__name__)


@exu.route('/python', strict_slashes=False)
@exu.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    exu.run(host='0.0.0.0', port='5000')
