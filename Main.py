import numpy as np
import pandas as pd
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!This is Revanth"

if __name__ == '__main__':
    app.run()