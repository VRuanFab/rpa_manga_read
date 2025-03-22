from app.pages.index import Pages
from app.utils.image_utils import ImagePil
from app.utils.windows_use import WinUse
from app.utils.prevencao_erros import Prevencao_erros
from app.utils.compactar_imagens import Compactar
from app.utils.toast import Aviso
from app.utils.cursesAssets import Curses
import time


class RunRPA(Pages):
    def __init__(self):
        self.prevenir = Prevencao_erros()

    def begin(self):
        self._definindoParametros()
        
        if self.terminar_em_capitulo == None:
            try:
                super().__init__(self.nome_manga, self.capitulo)
                self._passo1()
                self._passo2()
                self._passo3()
                self._passo4(self.capitulo)
                self._passo5(self.capitulo)
                self.fechar_navegador()
                try:
                    Aviso(self.nome_manga, self.capitulo).aviso_terminou()
                except:
                    pass
            except:
                # WinUse().os_use.remove(WinUse().path_to_folder('/app/assets/paginas'))
                Aviso(self.nome_manga, self.capitulo).smt_wrong()
                raise Exception('erro')
        else:
            for i in range(int(self.capitulo), int(self.terminar_em_capitulo) + 1):
                try:
                    super().__init__(self.nome_manga, i)
                    self._passo1()
                    self._passo2()
                    self._passo3()
                    self._passo4(capitulo=i)
                    self._passo5(capitulo=i)
                    self.fechar_navegador()
                    try:
                        Aviso(self.nome_manga, i).aviso_terminou()
                    except:
                        pass
                except Exception as err:
                    print(err)
                    Aviso(self.nome_manga, i).smt_wrong()
                    # WinUse().os_use.remove(WinUse().path_to_folder('/app/assets/paginas'))
        
    def _definindoParametros(self):
        self.terminar_em_capitulo = None
        
        self.nome_manga = str(input('Nome do mangá:\n'))
        yes_or_no = [
                    {'desc': 'Sim', 'value':True},
                    {'desc': 'Não', 'value': False}
                    ]
        varios_caps = Curses(yes_or_no).opcoes(header_text='Deseja baixar mais de um capitulo?')
        
        self.capitulo = str(input('\nCapítulo:\n')) if varios_caps == False else str(input('\nQual capitulo começar:\n'))

        if varios_caps == True:
            self.terminar_em_capitulo = str(input('\nAté capitulo:\n'))
        
        if WinUse().check_shortcut_exist() == False:
            self.criar_atalho = Curses(yes_or_no).opcoes('Deseja criar um atalho para a pasta de mangás em seu desktop (área de trabalho)?')
        else:
            self.criar_atalho = False
            
        # Curses().setString("Seu download está sendo feito")


    def _passo1(self):
        self.main_page.pesquisarManga(self.nome_manga)

    def _passo2(self):
        self.manga_selecionado.listaCapitulos()
        
    def _passo3(self):
        app = self.dentro_manga
        self.prevenir.check_pasta_existe('/app/assets/paginas')
        app.baixar()
        self.ordemPagina = app.retornarOrdem()
        
    def _passo4(self, capitulo):
        winApp = WinUse()
        pdfTransform = ImagePil(self.nome_manga, capitulo)
        self.prevenir.check_pasta_existe('/app/assets/paginas')
        self.prevenir.check_pasta_existe(f'/app/assets/manga_baixado/{self.nome_manga}')

        caminho_pdf = winApp.path_to_folder(f'/app/assets/manga_baixado/{self.nome_manga}')
        
        self.imagens = [nome_img for nome_img in self.ordemPagina]
        pdfTransform.criarPdf(self.imagens, caminho_pdf)

    def _passo5(self, capitulo):
        self.prevenir.check_pasta_existe(f'/app/assets/paginas_img_compactada/{self.nome_manga}')
        Compactar(file_list=self.imagens, nome_arquivo=f'{self.nome_manga} capitulo {capitulo}', nome_manga=self.nome_manga)
        
        for file in self.imagens:
            WinUse().os_use.remove(file)
        
        if self.criar_atalho:
            WinUse().criar_shortcut()