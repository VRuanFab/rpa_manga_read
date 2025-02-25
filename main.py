import time
from app.utils.navegador import Navegador


site = Navegador('https://www.google.com.br')
site.openNavegador()

elemento = site.procurarElemento('XPATH', "//*/textarea[@class='gLFyf']")
elemento.send_keys('Levi comprou uma casa bonitona')

time.sleep(348732)