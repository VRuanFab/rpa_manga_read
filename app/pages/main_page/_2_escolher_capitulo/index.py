import time


class Capitulos:
    def __init__(self, driver, capitulo):
        self.capitulo = capitulo
        self.driver = driver
        
        print('escolha seu capitulo')
        
    def listaCapitulos(self):
        time.sleep(1)
        botoes_auxiliar = self.driver.procurarArrayElementos('XPATH', "//*/div[@class='flex gap-x-2 mb-4']/button")[1]
        botoes_auxiliar.click()
        
        escolhendo_volume = self.driver.procurarElemento('XPATH', f"//*/h4[text()='Chapter {self.capitulo}']/../../../../../../../../../button")
        escolhendo_volume.click()
        
        time.sleep(2)
        
        pegando_capitulo = self.driver.procurarElemento('XPATH', f"//*/h4[text()='Chapter {self.capitulo}']/..")
        pegando_capitulo.click()
        
        escolhendo_idioma = self.driver.procurarElemento('XPATH', f"//*/h4[text()='Chapter {self.capitulo}']/../../../../../../../../..//*/img[@title='Portuguese (Br)']/../..")
        escolhendo_idioma.click()
        
        print(f'capitulo {self.capitulo}')
        time.sleep(348732)