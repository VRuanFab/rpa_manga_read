from app.utils.navegador import Navegador
from app.utils.windows_use import WinUse
from app.pages.main_page._1_enter.enter import AcessarPagina
from app.pages.manga_selecionado._1_escolher_capitulo.index import Capitulos
from app.pages.dentro_manga._1_baixar.index import BaixarImagens

class Pages(Navegador):
    def __init__(self, nome_anime, capitulo):
        self.driver = Navegador().openNavegador(WinUse().get_env('SITE'))
        
        self.main_page = AcessarPagina(self.driver)
        self.manga_selecionado = Capitulos(driver=self.driver, capitulo=capitulo)
        self.dentro_manga = BaixarImagens(driver=self.driver, nome_anime=nome_anime, capitulo=capitulo)
        
        
    def fechar_navegador(self):
        return super().fechar_navegador()