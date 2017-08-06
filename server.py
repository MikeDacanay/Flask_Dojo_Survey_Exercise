from flask import Flask, request, render_template, redirect, session, flash
app = Flask(__name__)
app.secret_key= "Jade"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def create_user():
	name=request.form['name']
	location=request.form['location']
	language=request.form['language']
	comment=request.form['comment']

	if len(request.form['name'])<1:
		flash("Name Field Empty!")

	if len(request.form['comment'])>=120:
		flash("Your comment is too long!")



	return render_template('result.html', name1=name, location1=location, favorite_language1=language, comment1=comment)
app.run(debug=True)