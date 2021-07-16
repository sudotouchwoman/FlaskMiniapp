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

@app.route('/', methods = ['GET'])
def okay_fine():
    return 'Booba'


@app.route('/estimation', methods = ['GET'])
def get_estimation():
    return getfile('estimation.json')


@app.route('/variants', methods = ['GET'])
def get_variants():
    return getfile('variants.json')

    
@app.route('/model', methods = ['GET'])
def get_model():
    return getfile('model.json')



if __name__ == '__main__':
    app.run(debug=True)