from flask import request, render_template, url_for, redirect
from website import app, db, models, bcrypt
from website.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
import traceback

board_members = [
	{
		"name": "Zack Seliger",
		"img": "/static/potatoe.jpg",
		"desc": "Zack oiasjf oisfj oasij feosij foijes ofijaseo fijseo fiosifj osijef oisajeofi asjefois jefoisj ef"
	},
	{
		"name": "Teresa Perez",
		"img": "/static/potatoe.jpg",
		"desc": "Teresa asj fisj efoiasj feoisaj efoisjae foisje fojs foisfje oisaj efoisjef oisef."
	},
	{
		"name": "Matthew Cummings",
		"img": "/static/potatoe.jpg",
		"desc": "OSHE FOSHJEFUHSOI FHIES HFIS HEF HSLEF HS HEFSH EFH SEUIHF UISEHF ESFOIS EHJOFIHES UIHFEISH FUISE HFUHESKUFHSKUEHF KUESHFKHESKUF HESKU HFKUES HFKUSH EFKUHESFKU HES"
	}
]

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
    return render_template('about.html', board=board_members)


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
        try:
            if request.method == 'POST':
                app.logger.info('POST')
                username = form.username.data
                hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                # add to database
                db.session.add(models.User(username=form.username.data, email=form.email.data, password=hashed_password))
                db.session.commit()
                app.logger.info('\n\nvalidated 34213t wqd\n\n')
                return redirect(url_for('home'), code=307)  # it took me way too long to figure out this damn code arg
            elif request.method == 'GET':
                app.logger.info('GET')
                return redirect(url_for('home', name=form.username.data))
        except:
            app.logger.info('\n\nAHHHHHHHHHHHH\n\n')
            app.logger.info(traceback.format_exc())

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.query.filter_by(email=form.email.data).first()
            db_password = user.password
            password = form.password.data.encode('utf-8')
            if user and bcrypt.check_password_hash(db_password, password):
                login_user(user)
                next_page = request.args.get('next')
                # app.logger.info(user.username)
                return redirect(next_page) if next_page else redirect(url_for('home', username=user.username))
            else:
                pass
                #flash('Login Unsuccessful. Please check email and password', 'danger')
        except:
            app.logger.info('\n\nAHHHHHHHHHHHH\n\n')
            app.logger.info(traceback.format_exc(),'\n\n')
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
