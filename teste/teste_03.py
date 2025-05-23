# Instalar Selenium e WebDriver Manager
!pip install -q selenium webdriver-manager

# Instalar o Chrome e Chromedriver
!apt-get update -qq > /dev/null
!apt install -y chromium-chromedriver > /dev/null
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

# Importar bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import unittest
import time

# Configurar navegador headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Teste Selenium com demoqa.com
class TestDemoQAForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.maximize_window()

    def test_preencher_formulario(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Fechar o banner de propaganda
        try:
            driver.execute_script("document.getElementById('fixedban').style.display='none'")
        except:
            pass

        # Preencher campos básicos
        driver.find_element(By.ID, "firstName").send_keys("Gabrielly")
        driver.find_element(By.ID, "lastName").send_keys("Silva")
        driver.find_element(By.ID, "userEmail").send_keys("gabrielly@example.com")
        driver.find_element(By.XPATH, "//label[contains(text(),'Female')]").click()
        driver.find_element(By.ID, "userNumber").send_keys("11999999999")

        # Preencher data de nascimento: 15 de maio de 2004
        driver.find_element(By.ID, "dateOfBirthInput").click()
        driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("2004")
        driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("May")
        driver.find_element(By.CLASS_NAME, "react-datepicker__day--015").click()

        # Scroll e submit
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.ID, "submit"))
        driver.find_element(By.ID, "submit").click()

        # Verifica modal de sucesso
        modal_title = wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))).text
        self.assertEqual(modal_title, "Thanks for submitting the form")

    def tearDown(self):
        self.driver.quit()

# Executar teste
unittest.main(argv=[''], exit=False)
