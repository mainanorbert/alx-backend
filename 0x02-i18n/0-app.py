#!/usr/bin/env python3
'''python module running flass apo'''

from flask import Flask, render_template
from typing import Any


app = Flask(__name__)


@app.route('/')
def index() -> Any:
    """rendering a template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
