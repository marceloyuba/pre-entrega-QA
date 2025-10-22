import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.saucedemo_functions import (
    login,
    validate_login,
    validate_inventory_page,
    add_first_product_to_cart,
    validate_cart
)

@pytest.fixture
def setup():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_success(setup):
    login(setup)
    validate_login(setup)

def test_inventory_page(setup):
    login(setup)
    validate_inventory_page(setup)

def test_add_to_cart(setup):
    """Test: Agregar producto al carrito y verificar."""
    login(setup)
    product_name, _ = validate_inventory_page(setup)
    add_first_product_to_cart(setup)
    validate_cart(setup, product_name)
