from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def hello():
  header = json.load(open('./templates/json/index/header.json'))
  cardInfos = json.load(open('./templates/json/index/cardInfos.json'))
  featured = json.load(open('./templates/json/index/featured.json'))
  return render_template('index.html', header=header, cardInfos=cardInfos, featured=featured)

@app.route('/cubing')
def cubing():
  return render_template('cubing.html')

@app.route('/languages')
def languages():
  return render_template('languages.html')

@app.route('/programming')
def programming():
  return render_template('programming.html')

@app.route('/blog')
def blog():
  return render_template('blog.html')

if __name__ == '__main__':
  app.run(debug=True)