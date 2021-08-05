from flask import *
from flask import url_for
import argparse
import requests
import os

app = Flask(__name__)


@app.route('/number-cats/<int:number>')
def main(number):
    urls = []
    directory = "static"

    parent_dir = '/Users/lenguyen/Desktop/ProjectFlask'
    path = os.path.join(parent_dir, directory)

    if not os.path.exists(path):
        os.mkdir(path)
    
    for i in range(number):
        location = os.path.join(path, 'cat' + str(i) + '.jpg')

        r = requests.get('https://cataas.com/cat')
        with open(location, 'wb') as f:
            f.write(r.content)
        urls.append(url_for('static', filename='cat' + str(i) + '.jpg', _external=True))
        

    return str(urls)


if __name__ == "__main__":
    app.run()
