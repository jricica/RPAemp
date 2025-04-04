from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def enviar_info(info):
    # Abre el navegador con la ruta correcta del chromedriver
    driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')

    # Accede a la página de entrada de datos
    driver.get("http://tupagina.com/")

    try:
        # Espera explícita hasta que el campo de número de factura esté visible
        campo_numero_factura = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "numero_factura"))
        )
        campo_numero_factura.send_keys(info["numero_factura"])

        # Rellenamos el campo de fecha
        campo_fecha = driver.find_element(By.NAME, "fecha")
        campo_fecha.send_keys(info["fecha"])

        # Rellenamos el campo total
        campo_total = driver.find_element(By.NAME, "total")
        campo_total.send_keys(info["total"])

        # Enviar el formulario (presionamos Enter)
        campo_total.send_keys(Keys.RETURN)

        # Opcionalmente, podemos esperar a que la página cargue o reciba una respuesta
        WebDriverWait(driver, 10).until(
            EC.url_changes(driver.current_url)
        )

    except Exception as e:
        print(f"Ocurrió un error al intentar enviar la información: {e}")
    
    finally:
        # Cierra el navegador después de realizar las acciones
        driver.quit()
