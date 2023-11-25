#!/usr/bin/python3
'''starts a Flask web application'''

from flask import Flask, render_template as templates

exu = Flask(__name__)


@exu.route('/number_template/<int:n>', strict_slashes=False)
def template_num(n):
    return templates('5-number.html', n=n)


if __name__ == '__main__':
    exu.run(host='0.0.0.0', port='5000')
