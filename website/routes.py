from flask import request, render_template, url_for, redirect
from website import app, db, models, bcrypt
from website.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required


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
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            #db.session.add(models.User(username=request.form['username'], email=request.form['email'], password=request.form['password']))
            db.session.add(models.User(username=form.username.data, email=form.email.data, password=hashed_password))
            db.session.commit()
            return redirect(url_for('home'), code=307)  # it took me way too long to figure out this damn code arg
        elif request.method == 'GET':
            app.logger.info('GET')
            return redirect(url_for('home', name=form.username.data))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)
