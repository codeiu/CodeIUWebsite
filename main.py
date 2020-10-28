from flask import Flask, request, render_template

app = Flask(__name__)

board_members = [
	{
		"name": "Zack Seliger"
	},
	{
		"name": "Teresa Perez"
	},
	{
		"name": "Matthew Cummings"
	}
]

@app.route('/')
def home():
	return render_template('home.html', title="Home")

@app.route('/about')
def about():
	return render_template('about.html', title="About", board=board_members)

@app.route('/calendar')
def calendar():
	return render_template('calendar.html', title="Calendar")

@app.route('/videos')
def videos():
	return render_template('videos.html', title="Videos")


if __name__ == "__main__":
	app.run(debug=True)