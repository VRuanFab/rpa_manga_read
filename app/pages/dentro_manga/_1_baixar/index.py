from app.utils.windows_use import WinUse
from app.utils.imageToPdf import Download_img
import time
import requests


class BaixarImagens:
    def __init__(self, driver, nome_anime, capitulo):
        self.winApp = WinUse()
        self.download = Download_img()
        self.driver = driver
        self.nome_anime = nome_anime
        self.capitulo = capitulo
        
        
    def baixar(self):
        self.driver.focar_pagina()
        time.sleep(2)
        self.driver.procurarElemento('XPATH', f"//*/div[@class='mx-auto h-full md--page  flex']//*")
        
        paginas = self.driver.procurarArrayElementos('XPATH', f"//*/div[@class='slider-dividers']/*")
        self.lenPaginas = len(paginas)
        
        self.listOrdem = []
        
        try:
            try:
                current_image = self.driver.procurarElemento('XPATH', "//*/img[@class='img sp limit-width limit-height mx-auto' and @style!='display: none;']")
            except:
                current_image = self.driver.procurarArrayElementos('XPATH', "//*/img[@class='img sp limit-width limit-height mx-auto']")[0]
            
            print('eis aqui a imagem:')
            print(current_image)
        except:
            pass
        
        b64Image = self.driver.exec_js(self.download.script, current_image)
        
        print(f'b64Img: {b64Image}')
        self.download.extract(b64Image)
        
        time.sleep(5326)
        
        # for page_number in range(len(paginas)):
        #     self.winApp.moveToMiddle()
        #     time.sleep(3)
        #     self.winApp.click('right')
        #     self.winApp.pressKey('down', presses=2)
        #     self.winApp.pressKey('enter')
            
        #     time.sleep(1)

        #     self.winApp.conectar_janela('Salvar como')
        #     self.winApp.escrever(self.winApp.salvar_arquivo('/app/assets/paginas', f'{self.nome_anime} cap {self.capitulo} pag {page_number + 1}.jpg', counterSlashes=True))
        #     self.winApp.pressKey('enter')
            
        #     time.sleep(1)
            
        #     if page_number < len(paginas) - 1:
        #         self.driver.exec_js("""document.querySelectorAll('div.md--reader-menu')[0].children[0].querySelectorAll('div.flex')[4].children[2].click()""")
        #         time.sleep(2)
            
            # self.listOrdem.append(self.winApp.salvar_arquivo('/app/assets/paginas', f'{self.nome_anime} cap {self.capitulo} pag {page_number + 1}.jpg', counterSlashes=True))
            
    def retornarOrdem(self):
        return self.listOrdem