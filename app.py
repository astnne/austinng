from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def hello():
  header = json.load(open('./templates/json/index/header/header.json'))
  cards = json.load(open('./templates/json/index/content/cards.json'))
  featured = json.load(open('./templates/json/index/content/featured.json'))
  return render_template('index.html', header=header, cards=cards, featured=featured)

@app.route('/speedcubing')
def cubing():
  return render_template('speedcubing.html')

@app.route('/languages')
def languages():
  return render_template('languages.html')

@app.route('/programming')
def programming():
  return render_template('programming.html')

@app.route('/blog')
def blog():
  header = json.load(open('./templates/json/blog/header/header.json'))
  cards = json.load(open('./templates/json/blog/content/cards.json'))
  return render_template('blog.html', header=header, cards=cards)

if __name__ == '__main__':
  app.run(debug=True)