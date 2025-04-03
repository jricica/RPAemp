from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def enviar_info(info):
    # Abre el navegador
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

    # Accede a la página de entrada de datos
    driver.get("http://tupagina.com/")

    # Encuentra los campos de formulario y rellénalos
    campo_numero_factura = driver.find_element_by_name("numero_factura")
    campo_numero_factura.send_keys(info["numero_factura"])

    campo_fecha = driver.find_element_by_name("fecha")
    campo_fecha.send_keys(info["fecha"])

    campo_total = driver.find_element_by_name("total")
    campo_total.send_keys(info["total"])

    # Enviar el formulario
    campo_total.send_keys(Keys.RETURN)
    
    # Cierra el navegador
    driver.quit()
