from selenium import webdriver
from pages.Auth import Auth
from pages.Add_to_cart import CartActions
from pages.Cart import Cart
from pages.Checkout import Checkout
from pages.Verifier import Verifier

def test_shopping_cart():
    driver = webdriver.Chrome()

    auth = Auth(driver)
    auth.login("standard_user", "secret_sauce")

    cart_actions = CartActions(driver)
    products = ["sauce-labs-backpack", "sauce-labs-bolt-t-shirt", "sauce-labs-onesie"]
    cart_actions.add_products_to_cart(products)

    cart = Cart(driver)
    cart.go_to_cart()
    cart.click_checkout()

    checkout = Checkout(driver)
    checkout.fill_form("Даниил", "Савищенко", "101000")

    verifier = Verifier(driver)
    verifier.verify_total("Total: $58.29")

    driver.quit()
