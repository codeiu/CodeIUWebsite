from flask import Flask, request, render_template, url_for, flash, redirect
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a303cd25b21ff329d8ec262b31d082c0'

@app.route('/', methods=['GET', 'POST'])
def home():
	name = ""
	if request.method == "POST":
		name = " " + request.form['username']
		app.logger.info(f'{name} is in')
	else:
		if request.args.get('username') is not None: name = " " + request.args.get('username')
	return render_template('home.html', name=name)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/calendar')
def calendar():
	return render_template('calendar.html')

@app.route('/videos')
def videos():
	return render_template('videos.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		app.logger.info('validated')
		if request.method == 'POST':
			app.logger.info('POST')
			username = request.form['username']
			return redirect(url_for('home'), code=307) 	# it took me way too long to figure out this damn code arg
		elif request.method == 'GET':
			app.logger.info('GET')
			return redirect(url_for('home',name=form.username.data)) 
	return render_template('register.html', form=form)


if __name__ == "__main__":
	app.run(debug=True)