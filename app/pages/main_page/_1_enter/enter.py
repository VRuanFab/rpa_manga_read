from app.utils.navegador import Navegador
import time

class AcessarPagina:
    def __init__(self, driver):
        self.driver = Navegador(driver)

    def pesquisarManga(self, nome_manga):
        time.sleep(2)
        nome_mange = nome_manga
        input_pesquisa = self.driver.procurarElemento('ID', 'header-search-input')
        input_pesquisa.send_keys(nome_mange)
        
        try:
            lista_de_pesquisa = self.driver.procurarArrayElementos('XPATH', "//*/div[@class='grid gap-2']//*/div[@class='dense-manga-container']/div[@class='font-bold text-lg line-clamp-1 break-all']")
            
            def strg_deform(str):
                str = str.lower().strip()
                str = str.replace(' ', '')
                return str
            
            for item in lista_de_pesquisa:
                pesquisa = nome_mange
                pesquisa = strg_deform(pesquisa)
                
                resultado_pesquisa = item.get_attribute('textContent')
                resultado_pesquisa = strg_deform(resultado_pesquisa)
                
                if pesquisa == resultado_pesquisa:
                    item.click()
                    

        except Exception as err:
            print(err)