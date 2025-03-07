import zipfile
from app.utils.windows_use import WinUse

class Compactar:
    def __init__(self, file_list, nome_arquivo):
        self.winApp = WinUse()
        self.caminho = self.winApp.path_to_folder('/app/assets/paginas_img_compactada', counterSlashes=True)

        self.nome = nome_arquivo
        self.file_list = file_list
        self.winApp._permicao(caminho=self.caminho, permicao=0o777)
        self.compactar_fotos(self.caminho, self.file_list)


    def compactar_fotos(self, path, file_list):
        with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as compactar:
            for file in file_list:
                compactar.write(file, arcname=self.nome)