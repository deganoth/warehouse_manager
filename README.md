
<img src = "https://raw.githubusercontent.com/deganoth/sales-hemorrhage/master/staric/images/readme_logo.png" target= "_blank" style="display: block; margin-left: auto; margin-right: auto; width: 50%;">

# Waerhouse Manger - A cross platform stock managment system.

## Link to the app hosted on Heroku. 
https://mewsik-shop-inventory.herokuapp.com/

## What is this?

This is a stock managment system showcasing the C.R.U.D functioanlity of MongoDB. It combines a MongoDB collection with a Flask based python web application. It provides any user the ability to manage a mongoBD collection of text based documents. In this instance, a collection of musical instrument shop products. The ability to create, read, update, delete and search are all available.

## UX

Designed for use across multiple platoforms, the app is primarily designed for tablet use, however It displays well on both desktop and mobile. A familiar dashboard style layout is used to provide quick statistics about current inventory. With interactive charts using Chart.js, the user can compare stock levels within categories. Whith a link in the navabar logo to return to the dashboard, along with respective links in both products and categories, app navigation feels natural. A burger icon with a pop out menu in the top left corner is always available should the user require it. A familiar look is seen throughout thanks to the Materialize stlye framework. Similar to bootstrap, it user classnames to display using the flexbox feature available in most modern browsers. Links to both Chart.js and Materialize are below.

https://www.chartjs.org/
https://materializecss.com/

### Design/ Functionality

With the modern workplace in mind, this app has been designed with a professional appearance. A memorable user interface was an essential requirement for quick access. The primary focus of this project was to manipulate single collection documents. A search function gives a wider scope for quickly manipulating documents, should the collection grow in size. Materialize has a limited but concise collection of icons. These were used along with a text link to visually represent each page of the app. The products page displays in a table, while the categories page is a list. Each item on both pages is available to edit with a yellow edit icon to the left. This is where the Update and Delete functions are available, per item.    

## Features

#### 1. Dashboard
A tidy but detailed collcetion of information relating to the MongoDB documents. A dashboard can be found on most stock managment systems. It remains the hub for stock information, and allows the user access to any part of the web app. A Call to action is present as the seach bar. This tells the user what this app is for, allowing them to start using it instantly. The interactive charts associate colours with products and categories. This visual association makes product or cateogry comparison quick and easy.

#### 2. Pop-out Menu
An addition to all pages of the app, this concise menu allows access to all features available. An associated icon beside each item is twinned on each page header, re enforcing the association for the user. Materialize addes interaction features to help the user navigate. A pointer hand appears when a selection is available to make, along with a slight darkening of the menu item background. While the menu is in use, an overlay blocks the page in use from interaction, allowing the menu to take center stage. 

#### 3. Interactive Charts
Charts were added to make interaction with the app more appealing to the user. Collection document information is displayed in an alternative format to the traditional table seen on the products page. Only certain fields from each document are displayed per table. In this case, the list of procduct name, categories names, brand names and their associated quantities. Tooltips are a built in feature of the Chart.js library. This creates a popup box upon hovering on each segment of the chart, detailing it's associated information. Below, the legend represents the selected information in a focused table format. A javascript function callback feature of Chart.js, upon clicking each item of the legend table, the associated segment in the chart above is removed. This re arranges the remaining segments to dispaly their comparison. 

#### 4. Search Bar
Having a quick way to access a data collection of any kind is crucial. This search bar is featured on the dashboard, products page and search results pages both empty and populated. It makes use of regular expressions form the python functions library. A string is taken as an input from a html form on each associated page. If a single word is input, this used as the search parameter. Flask_pymongo takes this word and uses a "find()" function to search the associated mongoDB collection. A cursor reads each line of each document. The results are then counted to verify if there are any at all. If results are found, a searchresults.html page is displayed, if none are found, a searchnull.html page is displayed. For multiple words in a string, each word is searched independantly. The design of the data colletion is such that the user would search for associated product types and brands, leading to a logical collection of seach results. These fields are already associated within the database. 

#### 5. C.R.U.D functionality
As the primary feature set of this app, the user can interact with the mongoDB collection via flask_pymongo, and the user of the Jinja templating language. To create, a reguest is made to post a new document to the mongoDB dictionary. The post method is taken from a html form. It's action is the associated flask_pymongo app_route. In this case, "{{url_for('insert_product')}}". The addproduct.html page is displayed upon requesting to add a new product. It contains the required fields associated with the mongoDB document structure. Upon entering the data, an "add product" button provides the post function, sending the data to the mongoDB collection. A redirect to the products pages reveals the new entry. Updating and deleting are accessed via the specific object ID of each product. An edit button appears beside each entry on the products page. This leads to a pre populated editproduct.html page. The data is inserted using a request per field method send to mongoDB in the app.py file. A html form is again used to make the action take place between flask_pymongo and mongoDB. Two buttons appear at the bottom of the editproduct page. Update, or delete. This provides a robust feature set for document manipulation. The same set of features is applied to the categories page.

#### 6. Sortable Table 
While understanding the sort function provided by w3schools, a smaller but similar sort arrow display function was created. It takes "n" as a parameter, much in the same way as the sort function. This allows multiple versions of the same function to be used within a html page. The table id is requested and set to a variable. Each tag name within the table is then targeted to change its class. This function can be called multiple times by inserting the associated "TH" cell number. In this instance, "Options" would be associated with "0", "Name" would be "1" and so on. While not directly associated with the sort app because of the default layout sent form mongoDB, the arrows change on each click represents the change in alphabetical direction of each column.

#### 7. Cross Platform Design
Wether using this app on mobile, tablet or desktop, its feature set is displayed accordingly. This is acheived through a combination of Materialize classes, and css media queries. Materialisze makes use of a class nameing system similar to that of Bootstrap. Rows and columns divided into 12 segments. Column widths can be pre determined per screen size. For example, "class = "col l4 m6 s12" " would yeild a column of 1/3 the row width on large screen, 1/6 on medium screen, and the full width on smaller screens. Materialize also makes use of a Card system for displaying content. This represents the rows and columns in a tidy way.

## Technologies Used for Development

### Development

##### Python 3.8 - https://www.python.org/
The language used for connecting between the flask based web app, and the mongoDB database. Flask_pymongo is a repository of functions designed to work with mongoDB. 
##### Javascript - https://www.javascript.com/
Primarily used for display purposes in this project, it provided me with chart.js to display the mongoDB data interactively in a user friendly manner.
##### HTML5/CSS3
These tools were used to create the basic layout of the webpage. 
##### Jinja - https://palletsprojects.com/p/jinja/
This templating language was used in conjunction with flask_pymongo. It allows access to the application routing created in the app.py file. Using Jinja, a link to teach defined function can be called. In addition, mongoDB can be accessed from defined variables within any function of the app.py file.
##### Sublime - https://www.sublimetext.com/
I made use of this text editor throughout development. A super felxible text editor designed for writing code. 
##### MongoDB - https://www.mongodb.com/
The primary data source for this project. It provides a dataset stored in collections then dictionaries, and finally documents within the dictionaries. Access can be granted through various languages using a "connection string" available on the dashboard. In this case, flask_pymongo made use of this connection string. Documentation is available at length, providing details on in depth collection manipulation.
##### Git/GitHub - https://github.com/deganoth
I made use of this to host my project. I communicated via cmd.exe to share all project files and folders, including this file.
##### Heroku - https://en.wikipedia.org/wiki/Heroku
Heroku is used to host apps in various languges. In this case, it provides a live version of the app.py python file. There are prerequisites to making use of this service. These include a requirements.txt file, Procfile and some python libraries including flask-pymongo and dnspython. A connection must be made via the local git repository and heroku also. This allows pushing the entire project to heroku for hosting.
##### cmd - https://en.wikipedia.org/wiki/Cmd.exe
Windows based terminal for inserting commands.
##### Chart.js - https://www.chartjs.org/
This javascript based library provides user friendly responsive charts for displaying data. Connecting the scripts to mongoDB made use of Jinja once again. The scripts had to remain on the selected .html page for use, along with the cdn link call. Once in place, 
##### JQuery - https://jquery.com/
A requirement for making use of Jinja via the flask_pymongo library. It allowed jinja based queries to be made in html documents, referring to flask_pymongo functions.

### Testing

#### Firebox/Chrome Developer tools/cmd
Making use of the inspector console to check functionality, and investigate errors was vital for a smooth running app. Cmd also revealed data errors locally. Included in the flask_pymongo, and in conjunction with Jinja is the Werkzeug error reporting system. It reveals errors in great detail. While testing visually on the following platforms:
* iPhone 5 - 8 
* Samsung Galax7 S5, S7, S8
* ChromeBook 10"
* iPad Mini
* iPad Pro
* iPad 2
Data errors and syntax problems were addressed using this error system.

#### Manual User Tests
App testers. My work colleagues provided primary feedback on functionailty. Since the app is based on the in house epostrader system, their input was essential. Some of the key issues were:
* **Searching** - With the help of my mentor, SPencer, a search function was created. It took a single input and interated through each document in the collection for matching results. While functional, a more indepth string based input was suggested. By taking the string and splitting it into words, this was achieved.
* **Data Layout** - Having charts render data made sense, but the data displayed didn't initially. Determining which fields to display proved difficult, until combing two together. Initially, categories was dispalyed on it's own. There was some repetition. I decided to put the brand name beside each category name. This allowed the user to see which brand in which category was on display.
* **Sorting tables** - Making use of a javascript library for this was tried initially, but it didn't display correctly due to materialize conflicts in class names. I decided to add some of the features from it manually via plain javascript functions. w3schools provided an excellent search function iterating through each row. Arrows were then added through swapping CSS classes using a javascript function. The arrow is actually a box border that changes from top to bottom, depending on the number of clicks.

#### Known Errors
While testing in all popular browsers, Firfox revealed a collection of errors within materialize; Error in parsing value for ‘-webkit-text-size-adjust’.  Declaration dropped. materialize.css:2155:29
Unknown property ‘-moz-text-decoration’.  Declaration dropped. materialize.css:2257:27
Unknown pseudo-class or pseudo-element ‘-ms-input-placeholder’.  Ruleset ignored due to bad selector. materialize.css:6113:2
Unknown pseudo-class or pseudo-element ‘-ms-input-placeholder’.  Ruleset ignored due to bad selector. materialize.css:6116:2
Unknown pseudo-class or pseudo-element ‘-webkit-autofill’.  Ruleset ignored due to bad selector. materialize.css:6554:28
Expected ‘none’, URL, or filter function but found ‘alpha(’.  Error in parsing value for ‘filter’.  Declaration dropped. materialize.css:7326:11
Unknown pseudo-class or pseudo-element ‘-ms-track’.  Ruleset ignored due to bad selector. materialize.css:7465:19
Unknown pseudo-class or pseudo-element ‘-ms-fill-lower’.  Ruleset ignored due to bad selector. materialize.css:7474:19
Unknown pseudo-class or pseudo-element ‘-ms-fill-upper’.  Ruleset ignored due to bad selector. materialize.css:7478:19
Unknown pseudo-class or pseudo-element ‘-ms-thumb’.  Ruleset ignored due to bad selector. materialize.css:7482:19
Unknown pseudo-class or pseudo-element ‘-ms-thumb’.  Ruleset ignored due to bad selector. materialize.css:7494:56
Error in parsing value for ‘letter-spacing’.  Declaration dropped. materialize.css:7516:19
Unknown property ‘-moz-osx-font-smoothing’.  Declaration dropped. icon:22:27

As can be seen, these relate specifically to Firefox not supporting certain css selectors and functions. On all other popular browsers, no console errors occur. Browsers include Opera, Chrome, Microsoft Edge and Safari

## Deployment
I made use of GitHub to host the project files. To contribute to or clone for learning purposes, git provides an option as the top right of the master repository. Heroku is used for live testing online. 
A link to the Heroku app is linked above.

Next, in the command window, install flask, dnspython and flask_pymongo using the command "sudo pip3 install" followed by each library name. Do it once per name.

To test locally, Python 3.8 must be installed on your device. This allows running of the app.py function. 
To allow python to be accessed form anywhere on your device, and in the case of Windows use cmd.exe, a tickbox in the python 3.8.1 installer stating "Add Python 3.8 to PATH" must be ticked. This adds Python functions to the current Windows session and can be executed using the cmd.exe. Once the flask app is created, simply run "python app.py". A local link will appear in the cmd window.

Next, the folder containing your project must be setup as a Git repository. upon opening cmd.exe, navigate to your desired drive and/or folder using the cd commands ,then enter the command "git init". This sets the lcoation as a git repository. 

A MongoDB database must be created for proper use of this app. In the app.py file, or Flask app, a link "[URI]" is created via the mongoDB database and Flask. This string is available in the mongoDB dashboard under the "connect" button. A string is created containing database information. It is recommended to set this string as an environment variable for deployment to github, for security purposes. This can be done using the "dontenv" python library. For heroku, it must remain in place.

Next the Heroku Command Line Interface (CLI) must be installed. This can be downloaded form the heroku website for Windows users. To login via cmd.exe, use "heroku login --interactive". This avoids the need for  abrowser window to open, and allows a login from the terminal

A heroku app must be created on the heroku website. Once created, details on how to connect and push updates to heroku are in the "deploy" tab in the app dashboard. In the settings tab, selected the "Reveal Configs" button to add a PORT and IP key name and value. for PORT, use "5000", for IP use 0.0.0.0. 

After this, navigate to the folder in which the project should be held in. Create a file called "app.py". The app must contain a line importing os "import os", importing flask "from flask import Flask" followed by an app instatiation "app = Flask(__name__)". For testing purposes, a single app_route can be used that returns a string "@app.route("/")". The roward slash indicates the root of the app. Then a function with some text returned "def hello():". Below this on a new indented line, "return "Hello". Finally, settting up the IP address and PORT number tells the system wehre to run the app "if __name__ = '__main__":" and on a new line "app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'), debug=True)". Leaving debug to true for testing is important. The PORT and IP values are set above in the herok app.

For all of this to work on Heroku, a requirements.txt file and Procfile must be created and pushed to heroku. For requirements, in the command window type "pip3 freeze --local > requirements.txt". This gets all the local libraries in use for running the app, and pushes them to heroku. For the Profcile, run the command "echo: web: python app.py > Procfile". It is important to have an uppercase P and no extension for heroku to access it. This file tells heroku what platform the app is designed to run on.

Finally, to setup what heroku calls "dynos", run the command "heroku ps:scale web=1". The dyno system runs the heroku app in a container. It's a self contained unit with it's own infrastructure. 

## Solutions found

### Tutorials
Using Jinja templating in javascript.
* https://www.patricksoftwareblog.com/creating-charts-with-chart-js-in-a-flask-application/

Getting a distint word form a string in MongoDB
* https://www.tutorialspoint.com/get-distinct-first-word-from-a-string-with-mongodb

Creating a html based search bar for searching through MongoDB using Flask.
* https://tinyurl.com/rd5ynmj

Setting the Chart.js legend in a different html div.
* https://demo.themekita.com/ready-pro/livepreview/documentation/plugins/chart.html
* https://jsfiddle.net/6muqvwxL/4/
* https://tinyurl.com/scbtn8v
* https://codepen.io/michiel-huiskens/pen/RRaRRv

Finding duplicate documents in MongoDB
* https://www.compose.com/articles/finding-duplicate-documents-in-mongodb/

Making rnadom colours generate for data tables
* https://tinyurl.com/so8y7dt

Securing personal credentials using the dontenv() function
* https://preslav.me/2019/01/09/dotenv-files-python/

Classy Space Shooter
* https://www.youtube.com/watch?v=jVlNZgX5fV8
* https://www.youtube.com/watch?v=U0K0YTifb1w	
* https://www.youtube.com/watch?v=cuSQnbZloFc
* https://www.youtube.com/watch?v=KQ2FhPKBOHI
* https://www.youtube.com/watch?v=qs5xmT6Upsc

### Ideas

Circular game world
* https://www.emanueleferonato.com/2018/09/10/html5-prototype-of-a-circular-endless-runner-featuring-double-jump-built-with-phaser-adding-particle-trails-explosions-and-camera-effects/

Space shooter
* https://yorkcs.com/2019/02/08/build-a-space-shooter-with-phaser-3-5/

Space shooter 2
* https://gamedevacademy.org/creating-mobile-games-with-phaser-3-and-cordova/

Night & day 
* https://www.joshmorony.com/how-to-create-a-day-night-cycle-in-phaser/

Following
* http://www.html5gamedevs.com/topic/38089-help-understanding-the-follower-object/

Rotating Object around Player
* http://www.html5gamedevs.com/topic/39497-rotate-game-objects-around-a-moving-object/

Matter.js
* https://github.com/mikewesthad/phaser-matter-collision-plugin#as-a-script

### Problems
Save and load games
* https://www.dynetisgames.com/2018/10/28/how-save-load-player-progress-localstorage/

Camera follow
* https://gamedevacademy.org/how-to-make-a-mario-style-platformer-with-phaser-3/

Scale to screen width
* https://www.joshmorony.com/how-to-scale-a-game-for-all-device-sizes-in-phaser/

Window scaling
* https://phaser.io/phaser3/devlog/136

Mobile controls
* https://swemyss.me/blog/phaser-3-mobile-controls

Focus window
* https://www.emanueleferonato.com/2019/01/09/html5-endless-runner-built-with-phaser-and-arcade-physics-step-4-adding-a-scrolling-parallax-background/

Mobile adaption
* http://www.lessmilk.com/tutorial/flappy-bird-phaser-3

Resize game window	
* http://www.html5gamedevs.com/topic/40267-scaling-the-game-to-fit-inner-window/

Resizing part 2
* https://phaser.discourse.group/t/game-scaling-resizing-example-v3/1555

Sprite Scaling
* https://phasergames.com/scaling-in-phaser-3/

On Screen Controls
* https://github.com/photonstorm/phaser-examples/blob/master/examples/input/virtual gamecontroller.js

Alternate Keys for movement
* http://www.html5gamedevs.com/topic/40607-how-to-replace-arrow-keys-with-wasd-movement/

Mobile controls
* http://www.html5gamedevs.com/topic/38496-how-make-virtual-button-in-phaser-3/

Offline package building
* https://gamedevacademy.org/phaser-progressive-web-apps-tutorial/

Using phaser 3 scale manager
* https://stackoverflow.com/questions/51518818/how-to-make-canvas-responsive-using-phaser-3

Group scaling
* https://labs.phaser.io/edit.html?src=src/game objects\group\set scale.js

Pick random sound from range
* http://www.html5gamedevs.com/topic/37506-pick-random-element/

Group physics
* https://labs.phaser.io/edit.html?src=src/physics/arcade/group set velocity y.js&v=3.19.0

Health bars
* https://labs.phaser.io/edit.html?src=src/game objects/graphics/health bars demo.js&v=3.19.0

Tween scaling
* https://phaser.io/examples/v3/view/game-objects/bitmaptext/static/width-and-height#

Z index
* http://labs.phaser.io/edit.html?src=src\depth sorting\z index.js

Make a new project in WAMP
* https://www.development-tutorial.com/create-new-project-wampserver/

Hitbox size
* https://phaser.discourse.group/t/how-to-alter-sprite-hitbox-in-sprite-animation/819

Bitmaptext making
* https://www.joshmorony.com/adding-custom-fonts-to-your-phaser-game/

Font load open type
* https://labs.phaser.io/edit.html?src=src/game objects/text/static/custom webfont.js&v=3.19.0

## Credits

* My Mentor, **Spencer Bariball** for showing me the ropes, and being a great teacher. 
* https://rexrainbow.github.io/phaser3-rex-notes/docs/site/ - A user fiendly version of the APIfriendlyntation
* https://codeinstitute.net/ - For making this possible.
* https://www.youtube.com/channel/UCoLblLUQbqjfCAmU13LbwHw - Luis Zuno. Easy to follow videos, great solutions.
* https://phaser.io/examples - It's always in the last place you look. Invaluable resource for knowing their own platform! 

### SFX
* https://freesound.org/people/kiddpark/sounds/201159/ - kiddpark
* https://freesound.org/people/Zott820/sounds/209578/ - Zott820
* https://freesound.org/people/Timbre/sounds/404028/ - Timbre
* https://freesound.org/people/broodmes/sounds/47962/ - broodmes
* https://freesound.org/people/creek23/sounds/75235/ - creek23
* https://www.youtube.com/watch?v=lZ_DyimkS54 - Jezz Bezos
* https://freesound.org/people/LudwigMueller/sounds/459164/ - LudwigMeuller
* https://freesound.org/people/gpag1/sounds/388822/ - gpag1
* https://freesound.org/people/SilverIllusionist/sounds/411172/ - SilverIllusionist

