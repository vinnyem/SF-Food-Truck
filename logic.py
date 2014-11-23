from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
import requests, json


app = Flask(__name__)

json_data = "http://data.sfgov.org/resource/rqzj-sfat.json"
@app.route('/')
def home():
	return render_template('home.html')
#	return 'Hello World!!'

@app.route('/welcome')
def welcome():
	return render_template('main.html')


@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials'
        else:
            return redirect(url_for('home'))
        return render_template('login.html', error=error)
    
@app.route('/sumz', methods=['GET','POST'])
def sumz():
    if request.method == 'POST':
        value_one = int(request.form['numberone'])
        value_two = int(request.form['numbertwo'])
        total = value_one + value_two
#        data = {"total": str(total)}
#        return jsonify(data)
        return render_template('sum.html', value=total)
    return render_template('sum.html')
    
@app.route('/sffoodtrucks', methods=['GET'])
def sffoodtrucks():
    r = requests.get(json_data)
    data = []
    dic = {}
    data += json.loads(r.content)
    for d in data:
        print d.get('address')
        dic[d.get('applicant')] = d
        
#    return Response(json.dumps(dic), mimetype='application/json')
#    return render_template('main.html', res = jsonify(sffoodtrucks=dic))
#    return render_template('main.html', sffoodtrucks=dic)
    return render_template('main.html', dat = data)

    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_nf.html'), 404


if __name__ == '__main__':
	app.run(debug=True)
    