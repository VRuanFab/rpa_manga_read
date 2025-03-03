from app.pages.main_page._1_enter.enter import AcessarPagina
from app.pages.manga_selecionado._1_escolher_capitulo.index import Capitulos
from app.pages.dentro_manga._1_baixar.index import BaixarImagens
from app.utils.imageToPdf import ImagePil
from app.utils.windows_use import WinUse
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
        self.passo4()

    def passo1(self):
        self.page.abrirPagina()
        time.sleep(5)
        self.page.pesquisarManga(self.nome_manga)

    def passo2(self):
        app = Capitulos(self.page, self.capitulo)
        app.listaCapitulos()
        
    def passo3(self):
        app = BaixarImagens(self.page, self.nome_manga, self.capitulo)
        app.baixar()
        self.ordemPagina = app.retornarOrdem()
        
    def passo4(self):
        winApp = WinUse()
        pdfTransform = ImagePil(self.nome_manga, self.capitulo)
        caminho_imagens = winApp.path_to_folder('/app/assets/paginas/')
        caminho_pdf = winApp.path_to_folder(f'/app/assets/manga_baixado')
        # imagens = winApp.listarPasta(caminho_imagens)
        
        imagens = [nome_img for nome_img in self.ordemPagina]
        pdfTransform.criarPdf(imagens, caminho_pdf)