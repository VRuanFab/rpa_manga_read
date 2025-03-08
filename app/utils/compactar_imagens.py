import zipfile
from app.utils.windows_use import WinUse

class Compactar:
    def __init__(self, file_list, nome_arquivo):
        self.winApp = WinUse()
        self.caminho = self.winApp.path_to_folder('/app/assets/paginas_img_compactada')

        self.nome_arquivo = nome_arquivo
        self.file_list = file_list
        self.winApp._permicao(caminho=self.caminho, permicao=0o777)
        self.compactar_fotos(self.caminho, self.file_list)


    def compactar_fotos(self, path, file_list):
        with zipfile.ZipFile(f'{path}/{self.nome_arquivo}.zip', 'w', zipfile.ZIP_DEFLATED) as compactar:
            for index in range(len(file_list)):
                compactar.write(file_list[index].replace('\\', '/'), arcname=f'{self.nome_arquivo} pagina {int(index) + 1}.jpg')