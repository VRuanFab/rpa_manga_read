from PIL import Image
from app.utils.windows_use import WinUse

class ImagePil:
    def __init__(self, nome_manga, capitulo):
        self.image = Image
        self.arrayImagem = []
        self.win = WinUse()
        self.pathToAssets = self.win.path_to_folder()
        self.nome_manga = nome_manga
        self.capitulo = capitulo
        
    def criarPdf(self, fotos: list, caminhoPdf: str):
        self.win._permicao(caminhoPdf, 0o777) ##PERMISSÃO TOTAL PARA CRIAR PDF NA PASTA
        
        caminhoPdf_salvar = f'{caminhoPdf}/{self.nome_manga} {self.capitulo}.pdf'
        
        try:
            fotos_pdf = [Image.open(img).convert("RGB") for img in fotos]
            
            fotos_pdf[0].save(caminhoPdf_salvar, save_all=True, append_images = fotos_pdf[1:])
        except Exception as err:
            print(err)