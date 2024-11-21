import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class TestWebApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configura Chrome amb Selenium
        options = Options()
        options.add_argument("--headless")  # Executa en mode sense capçalera (desactiva per veure el navegador)
        options.add_argument("--no-sandbox")  # Necessari en entorns CI/CD
        options.add_argument("--disable-dev-shm-usage")  # Evita problemes de memòria compartida
        service = Service("/usr/local/bin/chromedriver")  # Ruta del ChromeDriver
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.get("http://127.0.0.1:5000/")  # URL de l'aplicació Flask

    @classmethod
    def tearDownClass(cls):
        # Elimina el tancament automàtic del navegador
        print("El navegador es mantindrà obert. Tanca'l manualment si cal.")
        # cls.driver.quit()  # Comenta o elimina aquesta línia

    def test_form_submission(self):
        # Troba els camps del formulari i introdueix dades
        name_field = self.driver.find_element(By.NAME, "name")
        age_field = self.driver.find_element(By.NAME, "age")
        submit_button = self.driver.find_element(By.XPATH, '//input[@type="submit"]')

        name_field.send_keys("Joan")
        age_field.send_keys("30")
        submit_button.click()

        # Comprova el resultat
        result = self.driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Hola, Joan, tens 30 anys!", result)
        time.sleep(5)


if __name__ == "__main__":
    unittest.main()   

