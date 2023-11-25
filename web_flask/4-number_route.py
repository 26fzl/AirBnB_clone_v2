#!/usr/bin/python3
'''starts a Flask web application'''

from flask import Flask

exu = Flask(__name__)


@exu.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    exu.run(host='0.0.0.0', port='5000')
