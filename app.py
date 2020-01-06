import os
from flask import Flask, render_template, redirect, request, url_for, json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'shop_inventory'
app.config["MONGO_URI"] = 'mongodb+srv://root:Ornagy13@myfirstcluster-vsdxp.mongodb.net/shop_inventory?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')

# Display the dashboard.html as the primary webpage and retrieve the relevant data from mongoDB
@app.route('/get_dashboard')
def get_dashboard():
    return render_template('dashboard.html', 
    	products=mongo.db.products.find(), 
        categories=mongo.db.products.find(), 
    	manufacturers=mongo.db.products.find()
    	)

# Display the products.html webpage and retrieve the relevant data form mongoDB for display
@app.route('/get_products')
def get_products():
	return render_template('products.html', 
		products=mongo.db.products.find(), 
    	)

# Make use of the data required from mongo to create dropdown menues for use in creating a new product
@app.route('/add_product')
def add_product():
	return render_template('addproduct.html', 
		manufacturers=mongo.db.manufacturers.find(), 
		categories=mongo.db.categories.find(),
		suppliers=mongo.db.suppliers.find()
    	)

# Convert the information collected on the addproduct.html webpage and send it back to mongoDB for insertion
@app.route('/insert_product', methods=['POST'])
def insert_product():
	products = mongo.db.products
	products.insert_one(request.form.to_dict())
	return redirect(url_for('get_products'))

# determine between different products by calling on the object id stored with each product. 
@app.route('/edit_product/<product_id>')
def edit_product(product_id):
	the_product = mongo.db.products.find_one({'_id': ObjectId(product_id)})
	all_manufacturers = mongo.db.manufacturers.find()
	all_categories = mongo.db.categories.find()
	all_suppliers = mongo.db.suppliers.find()
	return render_template('editproduct.html', 
		product=the_product,
		manufacturers=all_manufacturers, 
		categories=all_categories,
		suppliers=all_suppliers)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    	port=os.environ.get('PORT'), 
    	debug=True)