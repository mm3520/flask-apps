from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def hello_world():
	author = "Wine"
	name = "Mike" 
	return render_template('index.html', author=author, name=name)
