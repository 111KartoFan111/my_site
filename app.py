from flask import Flask, request, render_template, redirect, url_for,flash,send_from_directory,abort,send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)