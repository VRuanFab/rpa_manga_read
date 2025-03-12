from app.utils.windows_use import WinUse

class Prevencao_erros:
    def __init__(self):
        self.winApp = WinUse()
        
    def check_pasta_existe(self, path: str):
        """ Tenta criar a pasta, caso já exista, não acontecerá nada """
        self.winApp.os_use.makedirs(self.winApp.path_to_folder(path), exist_ok=True)
    