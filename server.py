from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/process', methods=['POST'])
def create_user():
	name=request.form['name']
	location=request.form['location']
	language=request.form['language']
	comment=request.form['comment']
	return redirect('/result')

@app.route('/result')
def result():
	return render_template('result.html', name1=name, location1=location, favorite_language1=language, comment1=comment)

app.run(debug=True)