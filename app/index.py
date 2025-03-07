from app.pages.index import Pages
from app.utils.imageToPdf import ImagePil
from app.utils.windows_use import WinUse
from app.utils.prevencao_erros import Prevencao_erros
import time


class RunRPA(Pages):
    def __init__(self, nome_manga, capitulo):
        self.nome_manga = nome_manga
        self.capitulo = str(capitulo)
        super().__init__(self.nome_manga, self.capitulo)
        self.prevenir = Prevencao_erros()


    def begin(self):
        self.passo1()
        self.passo2()
        self.passo3()
        self.passo4()

    def passo1(self):
        self.main_page.abrirPagina()
        time.sleep(5)
        self.main_page.pesquisarManga(self.nome_manga)

    def passo2(self):
        self.manga_selecionado.listaCapitulos()
        
    def passo3(self):
        app = self.dentro_manga
        app.baixar()
        self.ordemPagina = app.retornarOrdem()
        
    def passo4(self):
        winApp = WinUse()
        pdfTransform = ImagePil(self.nome_manga, self.capitulo)
        self.prevenir.check_pasta_existe('/app/assets/paginas')
        self.prevenir.check_pasta_existe('/app/assets/manga_baixado')

        caminho_pdf = winApp.path_to_folder(f'/app/assets/manga_baixado')
        
        imagens = [nome_img for nome_img in self.ordemPagina]
        pdfTransform.criarPdf(imagens, caminho_pdf)