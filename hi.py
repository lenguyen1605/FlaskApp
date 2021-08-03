from flask import *
from flask import url_for
import argparse
import requests
import os

app = Flask('hi')

@app.route('/dog')
def main():
    urls = []
    number = request.args.get('number', type=int)
    for i in range(2):
        urls.append(url_for('static', filename='dog'+str(i)+'.jpg'))
    return str(urls)

if __name__ == '__main__':
    app.run()
