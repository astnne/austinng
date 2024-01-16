from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/index')
def index():
  return redirect()

@app.route('/cubing')
def cubing():
  return render_template('cubing.html')

@app.route('/languages')
def languages():
  return render_template('languages.html')

@app.route('/programming')
def programming():
  return render_template('programming.html')

if __name__ == '__main__':
  app.run(debug=True, port=8800)