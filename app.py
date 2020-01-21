import os, re
from flask import Flask, render_template, redirect, request, url_for, json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.code import Code
#from dotenv import load_dotenv
#load_dotenv()

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'shop_inventory'
app.config["MONGO_URI"] = 'mongodb+srv://root:Ornagy13@myfirstcluster-vsdxp.mongodb.net/shop_inventory?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')

# Display the dashboard.html as the primary webpage and retrieve the relevant data from mongoDB
@app.route('/get_dashboard')
def get_dashboard():
	return render_template('dashboard.html', 
		bar_name="Products",
		bar_quantity=mongo.db.products.find(),
		bar_colour=mongo.db.products.find(),
		bar_product=mongo.db.products.find(),
		doughnut_name="Categories",
		doughnut_quantity=mongo.db.products.find(),
		doughnut_colour=mongo.db.products.find(),
		doughnut_category=mongo.db.products.find(),
		)

# Products section 

# Display the products.html webpage and retrieve the relevant data form mongoDB for display
@app.route('/get_products')
def get_products():
	return render_template('products.html', 
		products=mongo.db.products.find()
		)

# search the products collection for matching products based on the product name description, manufacturer
@app.route('/search_products', methods=['POST'])
def search_products():
	search_input = request.form['input_search']
	search_split = search_input.split()
	
	for search_word in search_split:
		search_text = {
			"$or": [
				{"product_name": {'$regex': search_word, '$options':'i'}},
				{"product_description": {'$regex': search_word, '$options':'i'}},
				{"manufacturer_name": {'$regex': search_word, '$options':'i'}},
				{"supplier_name": {'$regex': search_word, '$options':'i'}},
				{"category_name": {'$regex': search_word, '$options':'i'}},
				{"product_status": {'$regex': search_word, '$options':'i'}},
				{"product_EAN": {'$regex': search_word, '$options':'i'}},
			]
		}

	results = mongo.db.products.find(search_text)
	has_results = results.count()

# determines wether the search has any values by taking the counted result and tesing it's value against 0
	if has_results != 0:
		return render_template('searchresults.html', 
			search_text=search_input, 
			results=results
		)
	else:
		return redirect(url_for('search_empty'))

@app.route('/search_empty')
def search_empty():
	return render_template('searchnull.html')

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
		suppliers=all_suppliers
		)

@app.route('/update_product/<product_id>', methods=["POST"])
def update_product(product_id):
	products = mongo.db.products
	products.update( {'_id': ObjectId(product_id)},
		{
		'product_name':request.form.get('product_name'),
		'product_description':request.form.get('product_description'),
		'manufacturer_name': request.form.get('manufacturer_name'),
		'supplier_name': request.form.get('supplier_name'),
		'category_name':request.form.get('category_name'),
		'product_price':request.form.get('product_price'),
		'product_quantity':request.form.get('product_quantity'),
		'product_status':request.form.get('product_status'),
		'product_EAN':request.form.get('product_EAN')
		})
	return redirect(url_for('get_products'))

@app.route('/delete_product/<product_id>', methods=["POST"])
def delete_product(product_id):
	mongo.db.products.remove({'_id': ObjectId(product_id)})
	return redirect(url_for('get_products')
		)

@app.route('/get_categories')
def get_categories():
	return render_template('categories.html',
		categories=mongo.db.categories.find()
		)

@app.route('/add_category')
def add_category():
	return render_template('addcategory.html',
		categories=mongo.db.categories.find(),
		)

@app.route('/insert_category', methods=['POST'])
def insert_category():
	categories = mongo.db.categories
	categories.insert_one(request.form.to_dict())
	return redirect(url_for('get_categories'))

@app.route('/update_category/<category_id>', methods=["POST"])
def update_category(category_id):
	categories = mongo.db.categoriess
	categories.update( {'_id': ObjectId(category_id)},
		{
		'category_name':request.form.get('category_name')
		})
	return redirect(url_for('get_categories'))


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
	the_category = mongo.db.categories.find_one({'_id': ObjectId(category_id)})
	return render_template('editcategory.html', 
		category=the_category,
		)

@app.route('/delete_category/<category_id>', methods=["POST"])
def delete_category(category_id):
	mongo.db.categories.remove({'_id': ObjectId(category_id)})
	return redirect(url_for('get_categories')
		)

if __name__ == '__main__':
	app.run(host=os.environ.get('IP'), 
		port=os.environ.get('PORT'), 
		debug=True)