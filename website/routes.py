from flask import request, render_template, url_for, redirect
from website import app, db, models
from website.forms import RegistrationForm


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
            db.session.add(models.User(username=request.form['username'], email=request.form['email'], password=request.form['password']))
            db.session.commit()
            return redirect(url_for('home'), code=307)  # it took me way too long to figure out this damn code arg
        elif request.method == 'GET':
            app.logger.info('GET')
            return redirect(url_for('home', name=form.username.data))
    return render_template('register.html', form=form)
