from app.utils.windows_use import WinUse
from app.utils.navegador import Navegador
from app.utils.image_utils import Download_img
import time


class BaixarImagens:
    def __init__(self, driver, nome_anime, capitulo):
        self.winApp = WinUse()
        self.download = Download_img()
        self.driver = Navegador(driver)
        self.nome_anime = nome_anime
        self.capitulo = capitulo
        
        
    def baixar(self):
        self.driver.focar_pagina()
        time.sleep(2)
        self.driver.procurarElemento('XPATH', f"//*/div[@class='mx-auto h-full md--page  flex']//*")
        
        paginas = self.driver.procurarArrayElementos('XPATH', f"//*/div[@class='slider-dividers']/*")
        self.lenPaginas = len(paginas)
        
        self.listOrdem = []
        
        for page_number in range(len(paginas)):
            
            try:
                try:
                    current_image = self.driver.procurarElementoVisivel('XPATH', "//*/img[@class='img sp limit-width limit-height mx-auto' and @style!='display: none;']", timeout=60)
                except:
                    current_image = self.driver.procurarElementoVisivel('XPATH', "//*/img[@class='img sp limit-width limit-height mx-auto']", timeout=60)
            except:
                pass
            
            time.sleep(1)
            
            b64Image = self.driver.exec_js(self.download.script, current_image)
            
            time.sleep(1)
            
            self.download.extract(b64Image, self.winApp.salvar_arquivo('/app/assets/paginas', f'{self.nome_anime} cap {self.capitulo} pag {page_number + 1}.jpg'))
            
            if page_number < len(paginas) - 1:
                self.driver.exec_js("""document.querySelectorAll('div.md--reader-menu')[0].children[0].querySelectorAll('div.flex')[4].children[2].click()""")
                time.sleep(2)
            
            self.listOrdem.append(self.winApp.salvar_arquivo('/app/assets/paginas', f'{self.nome_anime} cap {self.capitulo} pag {page_number + 1}.jpg', counterSlashes=True))
            
    def retornarOrdem(self):
        return self.listOrdem