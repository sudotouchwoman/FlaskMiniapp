from flask import Flask
import os


BASEDIR     = os.getcwd()
ENCODING    = 'utf-8'
HOST        = '0.0.0.0'
PORT        = 5000
DEBUG       = False
app = Flask(__name__)


def import_file(dir:str,filename:str):
    global BASEDIR
    global ENCODING
    path = os.path.join(BASEDIR, dir, filename)
    if os.path.isfile(path):
        with open(path, 'r', encoding=ENCODING) as confile:
            imported_data = confile.read()
        return imported_data
    else:
        raise FileNotFoundError


# this function is called when GET request is done to the server
# so, in return it merely loads needed file (here it is a json string)
# the string is later parsed in the app
# somehow, the load is faster when in is requested then during in-app load
# i can assume this happens as 2 apps are run in separate threads
# as laptop i am running them is 4C/8T
# it may also happen bc of a complicated exception handling i used
@app.route('/json/<page>', methods = ['GET'])
def get_content(page:str):
    return import_file('content', page+'.json')

# maybe some parts of configs should be loaded from the server
# for example, lists of items for selectboxes
# we cannot find out what to fetch in advance, eh?
# @app.route('/markup/<page>', methods = ['GET'])
# def get_markup(page:str):
#     return import_file('markup', page+'.json')


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)