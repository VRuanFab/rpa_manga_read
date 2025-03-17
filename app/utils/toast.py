from app.utils.windows_use import WinUse
from win10toast_click import ToastNotifier


class Aviso:
    def __init__(self, nome_manga):
        self.toaster = ToastNotifier()
        self.nome_manga = nome_manga
        
    def open_folder(self):
        WinUse().os_use.startfile(WinUse().path_to_folder(f'/app/assets/manga_baixado/{self.nome_manga}', counterSlashes=True))
    
    def aviso_terminou(self, ):
        self.toaster.show_toast(
            "Download Concluido",
            "Ver mangá",
            icon_path= None,
            duration= 10,
            callback_on_click=self.open_folder
        )