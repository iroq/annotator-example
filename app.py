from flask import Flask, send_from_directory, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

