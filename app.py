import os
from flask import Flask, render_template, request, url_for, json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'shop_inventory'
app.config["MONGO_URI"] = 'mongodb+srv://root:Ornagy13@myfirstcluster-vsdxp.mongodb.net/shop_inventory?retryWrites=true&w=majority'

mongo = PyMongo(app)

#@app.route('/')

@app.route('/')
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
		products=mongo.db.products.find(), 
    	)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    	port=os.environ.get('PORT'), 
    	debug=True)