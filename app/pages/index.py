from app.pages.main_page._1_enter.enter import AcessarPagina
from app.pages.manga_selecionado._1_escolher_capitulo.index import Capitulos
from app.pages.dentro_manga._1_baixar.index import BaixarImagens

class Pages:
    def __init__(self, nome_anime, capitulo):
        self.main_page = AcessarPagina()
        self.driver = self.main_page.driver
        
        self.manga_selecionado = Capitulos(driver=self.driver, capitulo=capitulo)
        self.dentro_manga = BaixarImagens(driver=self.driver, nome_anime=nome_anime, capitulo=capitulo)