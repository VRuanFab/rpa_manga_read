from app.utils.navegador import Navegador
import time

class AcessarPagina(Navegador):
    def __init__(self):
        self.site = 'https://mangadex.org/'
        super().__init__(self.site)
    
    def abrirPagina(self):
        super().openNavegador()

    def pesquisarManga(self, nome_manga):
        self.nome_manga = nome_manga
        input_pesquisa = super().procurarElemento('ID', 'header-search-input')
        input_pesquisa.send_keys(self.nome_manga)
        
        try:
            lista_de_pesquisa = super().procurarArrayElementos('XPATH', "//*/div[@class='grid gap-2']//*/div[@class='dense-manga-container']/div[@class='font-bold text-lg line-clamp-1 break-all']")
            
            def strg_deform(str):
                str = str.lower().strip()
                str = str.replace(' ', '')
                return str
            
            for item in lista_de_pesquisa:
                pesquisa = self.nome_manga
                pesquisa = strg_deform(pesquisa)
                
                resultado_pesquisa = item.get_attribute('textContent')
                resultado_pesquisa = strg_deform(resultado_pesquisa)
                
                if pesquisa == resultado_pesquisa:
                    item.click()
                    

        except Exception as err:
            print(err)