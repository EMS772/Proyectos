from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Configuración del driver
def set_up():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(executable_path="C:\\SeleniumDrivers\\chromedriver.exe")  # Ajusta la ruta al chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.get("https://localhost:7099/")

    return driver

def register(driver):
    wait = WebDriverWait(driver, 10)

    # Navegar a la URL del formulario de registro
    driver.get("https://localhost:7099/Cuenta/Register")
    wait_for_seconds(2)  # Espera para asegurar que la página está completamente cargada

    # Asegurarse de que el formulario esté cargado
    try:
        wait.until(EC.presence_of_element_located((By.ID, "registrationForm")))
    except Exception as e:
        print(f"Error al encontrar el formulario de registro: {e}")
        return

    # Completar el formulario de registro
    try:
        wait.until(EC.visibility_of_element_located((By.ID, "Nombre"))).send_keys("Trrt User")
        driver.find_element(By.ID, "Email").send_keys("trrtuser@example.com")
        driver.find_element(By.ID, "Password").send_keys("TrrtPassword123!")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("TrrtPassword123!")
    except Exception as e:
        print(f"Error al completar el formulario: {e}")
        return

    # Aceptar los términos si no está seleccionado
    try:
        terms_checkbox = driver.find_element(By.ID, "terms")
        if not terms_checkbox.is_selected():
            terms_checkbox.click()
    except Exception as e:
        print(f"Error al seleccionar el checkbox de términos: {e}")
        return

    # Hacer clic en el botón de enviar
    try:
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
    except Exception as e:
        print(f"Error al hacer clic en el botón de enviar: {e}")
        return

    # Esperar a que aparezca el mensaje de éxito
    try:
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Registro exitoso"))
        print("Registro exitoso")
    except Exception as e:
        print(f"Error al esperar el mensaje de éxito: {e}")

    # Navegar a la página de inicio
    driver.get("https://localhost:7099/")
    wait_for_seconds(2)  # Espera para asegurar que la página de inicio esté completamente cargada


# Iniciar sesión
def login(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://localhost:7099/")  # Asegúrate de que esta es la URL correcta para la página de login
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("trrtuser@example.com")
    driver.find_element(By.ID, "password").send_keys("TrrtPassword123!")
    driver.find_element(By.CSS_SELECTOR, "button.btn-dark").click()

    # Esperar a que se cargue la página de productos
    wait.until(EC.url_contains("Home/Index"))
    print("Inicio de sesión exitoso")

# Filtrar por categoría
def filter_by_category(driver, category):
    wait = WebDriverWait(driver, 10)

    try:
        # Mapeo de nombres de categorías a sus IDs
        category_mapping = {
            "Todos": None,
            "Deportes": "4",
            "Electrónica": "5",
            "Hogar": "6"
        }

        # Obtener el ID de la categoría
        category_id = category_mapping.get(category)

        # Construir el selector CSS basado en la categoría
        if category_id:
            selector = f"a.nav-link[href*='categoria={category_id}']"
        else:
            selector = "a.nav-link[href='/Home/Index']"

        # Desplazarse hacia abajo para hacer visibles las categorías
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)  # Esperar un momento para que se complete el desplazamiento

        # Esperar a que el enlace de la categoría esté presente y sea clickeable
        category_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        
        # Asegurarse de que el elemento esté en la vista
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", category_link)
        time.sleep(0.5)  # Pequeña pausa para asegurar que el elemento esté completamente visible
        
        # Hacer clic en el enlace de la categoría
        category_link.click()

        # Esperar a que se carguen los productos filtrados
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".row-cols-2")))
        
        print(f"Filtrado por categoría: {category}")

    except Exception as e:
        print(f"Error al filtrar por categoría: {e}")

    # Desplazar la página hacia el área de los productos
    product_section = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".row-cols-2")))
    driver.execute_script("arguments[0].scrollIntoView(true);", product_section)

    # Desplazar la página aún más hacia abajo para asegurarse de que más productos sean visibles
    for _ in range(3):
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(0.5)
# Ver detalles del producto
def view_product_details(driver):
    wait = WebDriverWait(driver, 10)

    # Desplazar la página hacia el área de los productos
    product_section = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".row-cols-2")))
    driver.execute_script("arguments[0].scrollIntoView(true);", product_section)

    # Desplazar la página aún más hacia abajo para asegurarse de que los productos sean visibles
    driver.execute_script("window.scrollBy(0, 500);")

    # Intentar hacer clic en el botón de detalles de un producto aleatorio
    detalle_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[onclick*='showInPopup']")))
    if detalle_buttons:
        random_index = random.randint(0, len(detalle_buttons) - 1)
        element_to_click = detalle_buttons[random_index]
        driver.execute_script("arguments[0].scrollIntoView(true);", element_to_click)

        # Esperar a que el elemento sea clicable
        wait.until(EC.element_to_be_clickable(element_to_click))

        try:
            element_to_click.click()
            print("Detalles del producto abiertos")
        except Exception:
            print("No se pudo hacer clic en el elemento, intentando otra estrategia...")
            driver.execute_script("arguments[0].click();", element_to_click)

        # Esperar a que se abra el modal
        wait.until(EC.presence_of_element_located((By.ID, "form-modal")))

        # Esperar un poco para simular la lectura de los detalles
        time.sleep(2)

        # Cerrar el modal de detalles
        close_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".modal .btn-close")))
        close_button.click()

        # Esperar a que se cierre el modal
        wait.until(EC.invisibility_of_element_located((By.ID, "form-modal")))
        print("Modal de detalles cerrado")
    else:
        print("No se encontraron botones de detalles")

# Añadir al carrito
def add_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    try:
        # Esperar y desplazar la página para asegurarse de que los botones de agregar al carrito sean visibles
        product_section = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".row-cols-2")))
        driver.execute_script("arguments[0].scrollIntoView(true);", product_section)

        # Obtener los botones de agregar al carrito y verificar su visibilidad
        add_to_cart_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.add-to-cart")))
        if add_to_cart_buttons:
            random_index = random.randint(0, len(add_to_cart_buttons) - 1)
            button_to_click = add_to_cart_buttons[random_index]
            driver.execute_script("arguments[0].scrollIntoView(true);", button_to_click)
            wait.until(EC.element_to_be_clickable(button_to_click))

            button_to_click.click()

            # Verificar que el producto se agregó al carrito
            wait.until(lambda d: d.find_element(By.ID, "carrito-cantidad").text not in ["", "0"])
            print("Producto agregado al carrito exitosamente")
        else:
            print("No se encontraron botones para agregar al carrito")
    except Exception as ex:
        print(f"Se produjo un error al agregar al carrito: {ex}")

# Ir al carrito
def go_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    try:
        # Hacer clic en el botón del carrito
        cart_button = wait.until(EC.presence_of_element_located((By.ID, "carrito-btn")))
        driver.execute_script("arguments[0].scrollIntoView(true);", cart_button)
        wait.until(EC.element_to_be_clickable(cart_button))

        cart_button.click()

        # Esperar a que se cargue la página del carrito
        wait.until(EC.url_contains("Carrito/MostrarCarrito"))
        print("Navegado a la página del carrito")
    except Exception as ex:
        print(f"Se produjo un error al ir al carrito: {ex}")

# Manipular el carrito
def manipulate_cart(driver):
    wait = WebDriverWait(driver, 10)

    # Aumentar la cantidad de un producto
    quantity_inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".quantity-input")))
    if quantity_inputs:
        random_input = random.choice(quantity_inputs)
        current_quantity = int(random_input.get_attribute("value"))
        random_input.clear()
        random_input.send_keys(str(current_quantity + 1))
        random_input.send_keys(Keys.TAB)  # Para disparar el evento de cambio
        print("Cantidad de producto aumentada")
        time.sleep(1)  # Esperar a que se actualice el subtotal

    # Eliminar un producto del carrito
    delete_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".eliminar-item")))
    if delete_buttons:
        delete_buttons[0].click()
        print("Producto eliminado del carrito")
        time.sleep(1)  # Esperar a que se actualice el carrito
        wait_for_seconds(2)

    # Hacer clic en Finalizar Compra
    finalizar_compra_btn = wait.until(EC.presence_of_element_located((By.ID, "finalizar-compra-btn")))
    finalizar_compra_btn.click()
    print("Clic en Finalizar Compra")

    wait_for_seconds(2)

    # Confirmar la compra en el modal de SweetAlert
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".swal2-confirm"))).click()
    print("Compra confirmada en el modal")

    wait_for_seconds(2)

    # Esperar a que aparezca el modal de confirmación final y hacer clic en OK
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".swal2-confirm"))).click()
    print("Confirmación final de la compra")


# Logout
def logout(driver):
    wait = WebDriverWait(driver, 20)

    try:
        # Hacer clic en el botón de usuario para mostrar el menú desplegable
        user_menu_button = wait.until(EC.element_to_be_clickable((By.ID, "navbarDropdown")))
        driver.execute_script("arguments[0].scrollIntoView(true);", user_menu_button)
        user_menu_button.click()

        # Esperar a que el botón de "Pedidos" sea visible y clickeable
        pedidos_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Pedidos")))
        driver.execute_script("arguments[0].scrollIntoView(true);", pedidos_link)
        pedidos_link.click()

        # Esperar a que la página de pedidos se cargue
        wait.until(EC.url_contains("Venta"))
        wait_for_seconds(2)

        # Volver al menú desplegable para hacer clic en "Logout"
        user_menu_button = wait.until(EC.element_to_be_clickable((By.ID, "navbarDropdown")))
        driver.execute_script("arguments[0].scrollIntoView(true);", user_menu_button)
        user_menu_button.click()
        driver.get("https://localhost:7099/")
        logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//form[@asp-controller='Cuenta' and @asp-action='Logout']/button[@type='submit']")))
        print(f"Número de botones de logout encontrados: {len(logout_button)}")


        # Hacer clic en el botón de Logout
        logout_button.click()
        print("Cierre de sesión exitoso")

        

    except Exception as ex:
        print(f"Se produjo un error al cerrar sesión: {ex}")

def wait_for_seconds(seconds):
    time.sleep(seconds)

if __name__ == "__main__":
    driver = set_up()
    register(driver)    
    login(driver)
    filter_by_category(driver, "Hogar")  # Ajusta la categoría según tu aplicación
    view_product_details(driver)
    add_to_cart(driver)
    go_to_cart(driver)
    manipulate_cart(driver)
    logout(driver)
    driver.quit()
