from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
import requests, json


app = Flask(__name__)

#Data given
json_data = "http://data.sfgov.org/resource/rqzj-sfat.json"

#Home
@app.route('/')
def home():
	return redirect(url_for('mobile_food_facility'))

@app.route('/sfmobilefoodfacility', methods=['GET'])
def mobile_food_facility():
    r = requests.get(json_data)
    food_truck_data = []
    dic = {}
    food_truck_data += json.loads(r.content)
    return render_template('main.html', dat = food_truck_data)


@app.route('/sfmobilefoodfacility/<string:applicantId>', methods=['GET'])
def get_food_facility(applicantId):
    print applicantId
    data = []
    r = requests.get(json_data)
    locationdata = []
    dic = {}
    dump = []
    data += json.loads(r.content)
    for d in data:
        
        objectId = d.get('objectid')
        if applicantId == objectId:
            latitude = d.get('latitude')
            longitude = d.get('longitude')
            applicant = d.get('applicant')
            address = d.get('address')
            fooditems = d.get('fooditems')
            if (address == None):
                address = '-'
            if (fooditems == None):
                footitems = '-'
            print address
            dic = {'latitude': latitude, 'longitude': longitude, 'applicant': applicant, 
                   'address': address, 'fooditems': fooditems}
            print dic
            break
    return render_template('main2.html', maploc = dic)
    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_nf.html'), 404


if __name__ == '__main__':
	app.run(debug=True)
    