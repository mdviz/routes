from application import app

from flask import render_template, jsonify, send_from_directory

from application import operations

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/runWestUrl/<filename>')
def runWestUrl(filename):
	result = operations.runRoutes(filename, 'WestUrl')
	return jsonify({'result': result})

@app.route('/runEastUrl/<filename>')
def runEastUrl(filename):
	result = operations.runRoutes(filename, 'EastUrl')
	return jsonify({'result': result})


@app.route('/getoutput')
def sendoutput():
	print "eee"
	return app.send_static_file('out/outputA.csv')

if __name__ == '__main__':
	app.run()