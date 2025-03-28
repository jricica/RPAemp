from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def run_bot(search_query):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Para que no abra la ventana del navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)  # Esperar a que carguen los resultados

        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        return [result.text for result in results[:5]]  # Retorna los primeros 5 títulos
    except Exception as e:
        return str(e)
    finally:
        driver.quit()
