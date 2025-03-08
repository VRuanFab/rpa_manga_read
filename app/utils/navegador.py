from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from app.utils.windows_use import WinUse

class Navegador:
    def __init__(self, otherDrive=None):
        if otherDrive != None:
            self.driver = otherDrive
            self.wait = WebDriverWait(self.driver, timeout=35)
    
    def openNavegador(self, link):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, timeout=35)

        self.driver.get(link)
        
    def __set_by(self, type):
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

    def procurarElemento(self, search_type: str, element: str):
        """ Procura pelo elemento ao carregar a página """
        tipo_pesquisa = self.__set_by(search_type)
        return self.wait.until(EC.presence_of_element_located((tipo_pesquisa, element)))

    def procurarArrayElementos(self, search_type: str, element: str):
        """ Retorna os childs de um elemento em array """
        
        tipo_pesquisa = self.__set_by(search_type)
        return self.wait.until(EC.presence_of_all_elements_located((tipo_pesquisa, element)))
    
    def procurarElementoVisivel(self, search_type: str, element: str):
        """ Espera o elemento estar visível na tela """
        
        tipo_pesquisa = self.__set_by(search_type)
        return self.wait.until(EC.visibility_of_element_located((tipo_pesquisa, element)))
        
    def exec_js(self, script: str):
        """ Executa funções em javascript """
        self.driver.execute_script(script)