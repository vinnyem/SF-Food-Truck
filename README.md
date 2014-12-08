<h1>SF-Food-Truck</h1>

<h3>Problem Description:</h3>
<p>Create a service that tells the user what types of food trucks might be found near a specific location on a map.
The data is available on DataSF: Food Trucks </p>

<h3>Execution: </h3>

<p> I had two design layouts in mind. Since I wanted to show case my whole stack, so I had to prioritize and decided to go for a simpler model. I decided to go with Flask, because its the best choice for small web applications. It gave me some leeway to concentrate more on the user interface. Had no prior experience working on Google Map APIs, not to mention, it was a good learning experience.

My initial layout was to include the HTML Geolocation which would have had made this application whole lot user friendly, when the user logs in the home screen, where he/she already will have few options on the map  based on the location. <p>

<h3> Technology Stack: </h3>

<ul>
<li>Flask Framework (0.10)
<li>Jinja2
<li>Python 2.7
<li>HTML5
<li>Javascript
<li>jquery
<li>CSS Bootstrapper
<li>Google Map v3 APIs
<li>Live App hosted using https://www.pythonanywhere.com/ 
</ul>

<h3> Run the App: </h3>

<p> <i>python logic.py </i> <br>
*Make sure you copied all other dependent files. </p>

<h3> Usage: </h3>

<p><b>Website Home: </b> http://vinny.pythonanywhere.com/sfmobilefoodfacility or just http://vinny.pythonanywhere.com <br>
Information of San Francisco’s mobile home facility can be found in the page. <br>
Click on the link of the Business name to be redirected to the page where you can find the location of the business. <br>
Business URL format: http://vinny.pythonanywhere.com/sfmobilefoodfacility/ #unique-id# <br> </p>

<h3> Issues & workarounds: </h3>

<p> The hosting server had issues pulling the json_data over http. So the json_file is fed as a text file. <br>
Bootstrapped CSS, didn’t get to modify much. <br>
<b>Browser Compatibility:</b> Works better with Google Chrome, Firefox, Safari on desktops and laptops (best viewed at 1400x700). Haven’t tested on IE or Opera. <br>
</p>

<h3> Improvements: </h3>

You can never get satisfied with improvements. My next set of improvements would be to
<ul>
<li> Add Geolocation to enhance the design
<li>Unit-tests should be integrated
<li>Design flow and data validation
<li>Ajax to dynamically query for the map locations
<li>Pagination (especially if data seem to increase)
<li>Improved Styling of webpages
</ul>
<b><i>Hope you'd enjoy it!</i></b>
