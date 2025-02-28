from PIL import Image
from app.utils.windows_use import WinUse

class ImagePil:
    def __init__(self):
        self.image = Image
        self.arrayImagem = []
        self.win = WinUse()
        self.pathToAssets = self.win.path_to_folder()
    
    def addImage(self, image):
        imagem = f'{self.pathToAssets}/{image}'
        