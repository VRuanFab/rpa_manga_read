import pyautogui
import os
from pywinauto import Application


class Os_use:
    def __init__(self):
        self.os_use = os
        super().__init__()
        
    def __current_path(self):
        return os.getcwd().replace('\\', '/')
    
    def path_to_folder(self, caminho=''):
        return f'{self.__current_path()}{caminho}'
    
    def salvar_arquivo(self, caminho, nome_arquivo, counterSlashes=False):
        if counterSlashes:
            return f'{self.path_to_folder(caminho=caminho)}/{nome_arquivo}'.replace('/', '\\')
        else:
            return f'{self.path_to_folder(caminho=caminho)}/{nome_arquivo}'

class WinAuto:
    def __init__(self):
        self.win_app = Application(backend='win32')
        super().__init__()
        
    def conectar_janela(self, nome_janela, timeout=4):
        self.win_app.connect(title= nome_janela, timeout= timeout)


class WinUse(Os_use, WinAuto):
    def __init__(self):
        self.autogui = pyautogui
        super().__init__()
        
    def pressKey(self, key, presses=1):
        self.autogui.press(keys= key, presses= presses)
        
    def escrever(self, texto, intervalo = 0.01):
        self.autogui.write(texto, interval=intervalo)
        
    def moveToMiddle(self):
        self.autogui.moveTo(self.autogui.size().width/2, self.autogui.size().height/2)
        
    def click(self, button='left'):
        self.autogui.click(button=button)