from flask import Flask, render_template, request, send_from_directory
import json
import Ninja_shop

app = Flask(__name__)

@app.route('/3/<path:path>')
def serve_ninja(path):
	return send_from_directory('3', path)

@app.route('/', methods=['GET', 'POST'])
def sort():
	if request.method == 'POST':
		#print json.loads(request.form['list'])
		#return request.form['list']
		list = json.loads(request.form['list'])
		list = Ninja_shop.main(list)
		return render_template('result.html',listl=list)

	else:
	   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)
