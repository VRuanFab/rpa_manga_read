from app.utils.windows_use import WinUse
from notifypy import Notify


class Aviso(Notify):
    def __init__(self, nome_manga, capitulo):
        super().__init__()
        self.nome_manga = nome_manga
        self.capitulo = capitulo
    
    def aviso_terminou(self):
        self.title="Mangá Baixado"
        self.message=f"Mangá {self.nome_manga} capitulo {self.capitulo} baixado com sucesso!"
        self.application_name="Download Mangá"
        self.icon= WinUse().path_to_folder('/imgs/manga_icon.ico', counterSlashes=True)
        self.send()
        
    def smt_wrong(self):
        self.title="Deu erro"
        self.message=f"Algo deu errado"
        self.application_name="Download Mangá"
        self.icon= WinUse().path_to_folder('/imgs/manga_icon.ico', counterSlashes=True)
        self.send()