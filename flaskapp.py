from flask import Flask
app = Flask(__name__)

@app.route('/')
def okay_fine():
    return 'Booba'

if __name__ == '__main__':
    app.run()