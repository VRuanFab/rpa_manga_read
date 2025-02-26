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

    def procurarElemento(self, search_type, element):
        match search_type:
            case 'XPATH':
                tipo_pesquisa = By.XPATH

            case 'ID':
                tipo_pesquisa = By.ID
                
            case 'LINK_TEXT':
                tipo_pesquisa = By.LINK_TEXT
            
            case 'NAME':
                tipo_pesquisa = By.NAME
                
            case 'CLASS_NAME':
                tipo_pesquisa = By.CLASS_NAME
                
            case 'TAG_NAME':
                tipo_pesquisa = By.TAG_NAME
        
        return self.wait.until(EC.presence_of_element_located((tipo_pesquisa, element)))
    
    def procurarArrayElementos(self, search_type, element):
        match search_type:
            case 'XPATH':
                tipo_pesquisa = By.XPATH

            case 'ID':
                tipo_pesquisa = By.ID
                
            case 'LINK_TEXT':
                tipo_pesquisa = By.LINK_TEXT
            
            case 'NAME':
                tipo_pesquisa = By.NAME
                
            case 'CLASS_NAME':
                tipo_pesquisa = By.CLASS_NAME
                
            case 'TAG_NAME':
                tipo_pesquisa = By.TAG_NAME
        
        return self.wait.until(EC.presence_of_all_elements_located((tipo_pesquisa, element)))