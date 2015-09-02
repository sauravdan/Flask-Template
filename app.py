from flask import Flask, redirect, url_for, render_template, request, jsonify,\
    flash, current_app
from flask.ext.bootstrap import Bootstrap


bootstrap=Bootstrap()

app = Flask(__name__)
bootstrap.init_app(app)

@app.route('/')
def index():
    return render_template('hacks/index.html')


if __name__ == '__main__': 
    app.debug = True
    app.run(host='0.0.0.0', port = 5000)
