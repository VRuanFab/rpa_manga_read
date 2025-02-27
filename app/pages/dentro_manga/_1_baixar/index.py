from app.utils.windows_use import WinUse
import time
import requests


class BaixarImagens:
    def __init__(self, driver):
        self.winApp = WinUse()
        self.driver = driver
        
        
    def baixar(self):
        time.sleep(2)
        element_img = self.driver.procurarArrayElementos('XPATH', f"//*/div[@class='mx-auto h-full md--page  flex']//*")
        
        # Array.from(document.querySelectorAll('div.mx-auto.h-full.md--page.flex')[0].children)
        
        for childs in element_img:
            print(childs.get_attribute('class'))

        # time.sleep(4)

        # self.winApp.moveToMiddle()
        
        # self.winApp.pressKey('down', presses=2)
        # self.winApp.pressKey('enter')
        
        print(f'esperando')
        time.sleep(348732)