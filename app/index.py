from app.pages.index import Pages
from app.utils.image_utils import ImagePil
from app.utils.windows_use import WinUse
from app.utils.prevencao_erros import Prevencao_erros
from app.utils.compactar_imagens import Compactar
import time


class RunRPA(Pages):
    def __init__(self):
        self.prevenir = Prevencao_erros()


    def begin(self):
        self._definindoParametros()
        self._passo1()
        self._passo2()
        self._passo3()
        self._passo4()
        self._passo5()
        
    def _definindoParametros(self):
        self.nome_manga = str(input('Nome do mangá:\n'))
        self.capitulo = str(input('\nCapítulo:\n'))
        
        if WinUse().check_shortcut_exist() == False:
            self.criar_atalho = str(input('Deseja criar um atalho para a pasta de mangás em seu desktop (área de trabalho)? (S ou N)'))
            self.criar_atalho = False if self.criar_atalho.lower() == 'n' else True
        else:
            self.criar_atalho = False

        super().__init__(self.nome_manga, self.capitulo)


    def _passo1(self):
        self.main_page.pesquisarManga(self.nome_manga)

    def _passo2(self):
        self.manga_selecionado.listaCapitulos()
        
    def _passo3(self):
        app = self.dentro_manga
        self.prevenir.check_pasta_existe('/app/assets/paginas')
        app.baixar()
        self.ordemPagina = app.retornarOrdem()
        
    def _passo4(self):
        winApp = WinUse()
        pdfTransform = ImagePil(self.nome_manga, self.capitulo)
        self.prevenir.check_pasta_existe('/app/assets/paginas')
        self.prevenir.check_pasta_existe(f'/app/assets/manga_baixado/{self.nome_manga}')

        caminho_pdf = winApp.path_to_folder(f'/app/assets/manga_baixado/{self.nome_manga}')
        
        self.imagens = [nome_img for nome_img in self.ordemPagina]
        pdfTransform.criarPdf(self.imagens, caminho_pdf)

    def _passo5(self):
        self.prevenir.check_pasta_existe(f'/app/assets/paginas_img_compactada/{self.nome_manga}')
        Compactar(file_list=self.imagens, nome_arquivo=f'{self.nome_manga} capitulo {self.capitulo}', nome_manga=self.nome_manga)
        
        for file in self.imagens:
            WinUse().os_use.remove(file)
        
        if self.criar_atalho:
            WinUse().criar_shortcut()