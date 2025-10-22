from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver, user="standard_user", password="secret_sauce"):
    """Abre la página de login e ingresa credenciales válidas."""
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def validate_login(driver):
    """Valida que el login fue exitoso verificando /inventory.html y el título."""
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url
    assert "Swag Labs" in driver.title


def validate_inventory_page(driver):
    """Verifica el título de la página y la presencia de productos."""
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"

    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0, "No se encontraron productos"

    first_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    first_price = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text

    print(f"Primer producto encontrado: {first_name} - {first_price}")
    return first_name, first_price


def add_first_product_to_cart(driver):
    """Agrega el primer producto al carrito y valida el contador."""
    first_button = driver.find_element(By.XPATH, "(//button[contains(text(),'Add to cart')])[1]")
    first_button.click()
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1", "El contador del carrito no se actualizó correctamente"


def validate_cart(driver, expected_product):
    """Abre el carrito y valida que el producto agregado esté presente."""
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
    product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert product_name == expected_product, f"Se esperaba '{expected_product}', pero se encontró '{product_name}'"



