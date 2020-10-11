from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
	name = request.args.get('name')
	if name is None:
		name = "World"
	return 'Hello '+name+'!'

@app.route('/page1')
def page1():
	return render_template('page1.html', name="Zack")

if __name__ == "__main__":
	app.run(debug=True)