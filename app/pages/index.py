from app.pages.main_page._1_enter.enter import AcessarPagina
from app.pages.manga_selecionado._1_escolher_capitulo.index import Capitulos
from app.pages.dentro_manga._1_baixar.index import BaixarImagens

class Pages:
    def __init__(self):
        self.main_page = AcessarPagina()
        
    def manga_selecionado(self, driver, capitulo):
        return Capitulos(driver, capitulo)
    
    def dentro_manga(self, driver, nome_anime, capitulo):
        return BaixarImagens(driver, nome_anime, capitulo)