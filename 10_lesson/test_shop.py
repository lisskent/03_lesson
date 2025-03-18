import allure
from selenium import webdriver
from Pages.Auth import Auth
from Pages.Add_to_cart import CartActions
from Pages.Cart import Cart
from Pages.Checkout import Checkout
from Pages.Verifier import Verifier

@allure.title("Тест процесса покупки в интернет-магазине")
@allure.description("Проверка добавления товаров в корзину, оформления заказа и итоговой суммы")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopping_cart():
    driver = webdriver.Chrome()
    try:
        with allure.step("Авторизация пользователя"):
            auth = Auth(driver)
            auth.login("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину"):
            cart_actions = CartActions(driver)
            products = ["sauce-labs-backpack", "sauce-labs-bolt-t-shirt", "sauce-labs-onesie"]
            cart_actions.add_products_to_cart(products)

        with allure.step("Переход в корзину и начало оформления"):
            cart = Cart(driver)
            cart.go_to_cart()
            cart.click_checkout()

        with allure.step("Заполнение формы оформления заказа"):
            checkout = Checkout(driver)
            checkout.fill_form("Даниил", "Савищенко", "101000")

        with allure.step("Проверка итоговой суммы заказа"):
            verifier = Verifier(driver)
            verifier.verify_total("Total: $58.29")
    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()