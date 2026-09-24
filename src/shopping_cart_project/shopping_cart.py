from .products import Product
from pymongo import MongoClient
from loguru import logger


class ShoppingCart:

    def __init__(self):
        mongo_url = "mongodb+srv://gdsprasanth06_db_user:Gdsprasanth@1@cluster0.s6waley.mongodb.net/?appName=Cluster0"
        

        mongo_client = MongoClient(mongo_url)
        cart_db = mongo_client['cart']
        self.cart_collection = cart_db['cart_collection']

    def add_product(self,product:Product):
        self.cart_collection.insert_one(product.to_dict())
        logger.success(f"{product.name} was added to the database")
        


    def remove_product(self,product_name:str):
        self.cart_collection.delete_many({"name": product_name})
        logger.warning(f"{product_name} was removed from cart")



    def calculate_total(self,):
        all_items_cursor =  self.cart_collection.find()
        total = 0
        for item in all_items_cursor:
            total += item['price'] * item['quantity']

        logger.info(f"Your cart total is {total}")
        return total