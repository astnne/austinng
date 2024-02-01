from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
  cardInfos = [
    ["https://i.imgur.com/2BMBtLz.png", 
     "Cubing", 
     "Austin moves his fingers.", 
    "https://www.worldcubeassociation.org/persons/2023NGAU01", 
     "View Austin's WCA Profile", 
     "/cubing",
     "January 18, 2024 at 1:20AM"], #cubing
    ["https://i.imgur.com/1481ERD.jpg",
     "Languages",
     "Austin loves to speak Chinese.",
     "https://upimg.baike.so.com/doc/4160593-4360651.html",
     "View About Austin's School in China",
     "January 18, 2024 at 1:28AM"], #languages
    ["https://i.imgur.com/VHHLDjr.png",
     "Programming",
     "Austin moves his fingers. Again.",
     "https://astnne.github.io/",
     "View Austin's Other Website",
     "January 18, 2024 at 1:33AM"] #programming
  ]

  return render_template('index.html', cardInfos=cardInfos)

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