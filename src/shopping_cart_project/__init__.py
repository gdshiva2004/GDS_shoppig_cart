from .shopping_cart import ShoppingCart
from .products import Product
import time

def main():
    cart = ShoppingCart()

    ## Sample Product
    p1 = Product("iPhone Duo", 400000, 2)
    p2 = Product("Samsung Galaxy s26", 120000, 5)
    cart.add_product(p1)
    time.sleep(2)
    cart.add_product(p2)
    time.sleep(2)
    cart.calculate_total()
    
   

if __name__ == "__main__":
    main()