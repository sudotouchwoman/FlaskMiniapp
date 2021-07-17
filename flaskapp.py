from flask import Flask
import os


BASEDIR     = os.getcwd()
ENCODING    = 'utf-8'
HOST        = '0.0.0.0'
PORT        = 5000
DEBUG       = False
app = Flask(__name__)


def import_file(filename:str):
    global BASEDIR
    global ENCODING
    path = os.path.join(BASEDIR, 'content', filename)
    if os.path.isfile(path):
        with open(path, 'r', encoding=ENCODING) as confile:
            imported_data = confile.read()
        return imported_data
    else:
        raise FileNotFoundError


@app.route('/json/<content>', methods = ['GET'])
def get_content(content:str):
    return import_file(content+'.json')


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)