#!/usr/bin/python3
'''starts a Flask web application'''

from flask import Flask

exu = Flask(__name__)


@exu.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    exu.run(host='0.0.0.0', port='5000')
    
