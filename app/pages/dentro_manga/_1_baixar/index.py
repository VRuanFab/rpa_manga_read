from app.utils.windows_use import WinUse
import time
import requests


class BaixarImagens:
    def __init__(self, driver):
        self.winApp = WinUse()
        self.driver = driver
        
        
    def baixar(self):
        time.sleep(2)
        self.driver.esperarVisibilidade('XPATH', f"//*/div[@class='mx-auto h-full md--page  flex']//*")
        
        paginas = self.driver.procurarArrayElementos('XPATH', f"//*/div[@class='slider-dividers']/*")
        
        print('ta baixado')
        print(paginas.get_attribute('class'))
        
        time.sleep(1.5)
        
        
        print("teste array para baixar a cada página")
        time.sleep(4325)

        self.winApp.moveToMiddle()
        
        self.winApp.click('right')
        self.winApp.pressKey('down', presses=2)
        self.winApp.pressKey('enter')
        
        time.sleep(1)

        self.winApp.conectar_janela('Salvar como')
        
        self.winApp.escrever(self.winApp.salvar_arquivo('/app/assets', 'Dan da Dan', counterSlashes=True))
        
        self.winApp.pressKey('enter')
        
        print(f'esperando')
        time.sleep(348732)