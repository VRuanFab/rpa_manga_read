from app.pages.main_page._1_enter.enter import AcessarPagina
from app.pages.manga_selecionado._1_escolher_capitulo.index import Capitulos
from app.pages.dentro_manga._1_baixar.index import BaixarImagens
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
        self.passo3()

    def passo1(self):
        self.page.abrirPagina()
        time.sleep(5)
        self.page.pesquisarManga(self.nome_manga)

    def passo2(self):
        app = Capitulos(self.page, self.capitulo)
        app.listaCapitulos()
        
    def passo3(self):
        BaixarImagens(self.page).baixar()