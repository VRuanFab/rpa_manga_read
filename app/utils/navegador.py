from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class Navegador:
    def __init__(self, link):
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--start-maximized')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, timeout=35)
        self.link = link
        
    def openNavegador(self):
        self.driver.get(self.link)
        
    def set_by(self, type):
        match type:
            case 'XPATH':
                return By.XPATH

            case 'ID':
                return By.ID
                
            case 'LINK_TEXT':
                return By.LINK_TEXT
            
            case 'NAME':
                return By.NAME
                
            case 'CLASS_NAME':
                return By.CLASS_NAME
                
            case 'TAG_NAME':
                return By.TAG_NAME

    def procurarElemento(self, search_type, element):
        tipo_pesquisa = self.set_by(search_type)
        return self.wait.until(EC.presence_of_element_located((tipo_pesquisa, element)))

    def esperarVisibilidade(self, search_type, element):
        tipo_pesquisa = self.set_by(search_type)
        return self.wait.until(EC.presence_of_element_located((tipo_pesquisa, element)))

    def procurarArrayElementos(self, search_type, element):
        tipo_pesquisa = self.set_by(search_type)
        return self.wait.until(EC.presence_of_all_elements_located((tipo_pesquisa, element)))