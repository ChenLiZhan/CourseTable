from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	dates = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	times = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	return render_template('index.html', dates = dates, times = times)



if __name__ == '__main__':
	app.run(debug = True)