import os
from flask import Flask, render_template, redirect, request, url_for, json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'shop_inventory'
app.config["MONGO_URI"] = 'mongodb+srv://root:Ornagy13@myfirstcluster-vsdxp.mongodb.net/shop_inventory?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')

@app.route('/get_dashboard')
def get_dashboard():
    return render_template('dashboard.html', 
    	products=mongo.db.products.find(), 
        categories=mongo.db.products.find(), 
    	manufacturers=mongo.db.products.find()
    	)

@app.route('/get_products')
def get_products():
	return render_template('products.html', 
		products=mongo.db.products.find(), 
    	)

@app.route('/add_product')
def add_product():
	return render_template('addproduct.html', 
		manufacturers=mongo.db.manufacturers.find(), 
		categories=mongo.db.categories.find(),
		suppliers=mongo.db.suppliers.find()
    	)

@app.route('/insert_product', methods=['POST'])
def insert_product():
	products = mongo.db.products
	products.insert_one(request.form.to_dict())
	return redirect(url_for('get_products'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    	port=os.environ.get('PORT'), 
    	debug=True)