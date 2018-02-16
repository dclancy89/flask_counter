from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "jkl39e8huf38hf3ofnljfshoiu3"



@app.route('/')
def index():
	if session.get('num') is None:
		session['num'] = 1
	else:
		session['num'] += 1
	return render_template('index.html')

@app.route('/plustwo', methods=['POST'])
def plus_two():
	session['num'] += 1
	return redirect('/')

@app.route('/reset', methods=['POST', 'GET'])
def reset():
	session['num'] = 0
	return redirect('/')

app.run(debug=True)