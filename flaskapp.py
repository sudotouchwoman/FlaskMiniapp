from flask import Flask, request, jsonify
import os


app = Flask(__name__)
BASEDIR = os.getcwd()
ENCODING = 'utf-8'


def getfile(filename:str):
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
    return getfile(content+'.json')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)