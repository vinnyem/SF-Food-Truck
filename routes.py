from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

       <link href="static/bootstrap.css" rel="stylesheet" media="screen">

@app.route('/')
def home():
	return render_template('home.html')
#	return 'Hello World!!'

@app.route('/welcome')
def welcome():
	return render_template('home.html')


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
    

    
@app.route('
if __name__ == '__main__':
	app.run(debug=True)
    
           
           data = []
    elems = []
    data += json.loads(r.content)
    for d in data:
        print d
           jsonify(sffoodtrucks=data)
           
           or k,v in d.iteritems():
        
            print k,v
            break
        break
           
           #    for d in data:
    elems = json.dumps(data)
#    print elems
    
#    for k,v in elems.iteritems():
        
        print k,v
        break
           
           
                   {% if res %}
        
            {% for address in res.all %}
            
                <p>{{applicant['applicant']}}</p>

            
            {% endfor %}
        {% else %}
        <p> Sorry couldn't find any addresses</p>
    {% endif %}
           
               <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script>
      $(function(){
        // Get json response
        $('.json').click(function(){
          $.getJSON('/sffoodtrucks', function (ret) {
            alert('JSON got: ' + JSON.stringify(ret));
          });
        });
      });
           
           for (var address in dat){
            if (dat.hasOwnProperty(address)){
                console.log("hey");
            }
        }
           
           <style type="text/css">
    html, body {
      height: 100%;
      margin: 0;
      padding: 0;
    }

    #map_canvas {
      height: 100%;
    }

    @media print {
      html, body {
        height: auto;
      }

      #map_canvas {
        height: 650px;
      }
    }
    </style>
           
           
           <style type="text/css">
      html, body, #map-canvas { height: 100%; margin: 0; padding: 0;}
    </style>