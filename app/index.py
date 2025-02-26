from app.pages.main_page._1_enter.enter import AcessarPagina
from app.pages.manga_selecionado._1_escolher_capitulo.index import Capitulos
import time


class RunRPA():
    def __init__(self, nome_manga, capitulo):
        self.nome_manga = nome_manga
        self.capitulo = str(capitulo)
        self.page = AcessarPagina()
        print('rpa running')
        
        
        
    def begin(self):
        self.passo1()
        self.passo2()

    def passo1(self):
        self.page.abrirPagina()
        time.sleep(5)
        self.page.pesquisarManga(self.nome_manga)

    def passo2(self):
        app = Capitulos(self.page, self.capitulo)
        app.listaCapitulos()