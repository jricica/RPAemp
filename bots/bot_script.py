from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# Configuración de opciones para Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Iniciar Chrome maximizado

# Iniciar el navegador con el controlador de Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Navegar a la página de login
    driver.get("URL_DE_TU_SITIO_WEB")  # Sustituye con la URL de la página

    # Esperar hasta que el campo de nombre de usuario esté presente
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    
    # Ingresar el nombre de usuario
    username_field.send_keys("admin")  # Sustituye con el nombre de usuario que quieras ingresar

    # Esperar hasta que el campo de contraseña esté presente
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    
    # Ingresar la contraseña
    password_field.send_keys("password123")  # Sustituye con la contraseña que quieras ingresar

    # Si es necesario, enviar el formulario
    password_field.send_keys(Keys.RETURN)  # O puedes usar un botón en lugar de esto

    # Esperar a que la página de inicio se cargue (esto depende del sitio web)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "elemento_que_indica_que_iniciaste_sesion"))
    )

    # Realizar alguna acción después de iniciar sesión, por ejemplo, cerrar sesión
    print("Inicio de sesión exitoso")

finally:
    # Espera algunos segundos y cierra el navegador (puedes ajustar el tiempo)
    driver.implicitly_wait(5)
    driver.quit()
