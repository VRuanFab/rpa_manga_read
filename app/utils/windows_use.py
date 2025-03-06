import pyautogui
import os
import keyboard
from pywinauto import Application


class Os_use:
    def __init__(self):
        self.os_use = os
        super().__init__()
        
    def __current_path(self):
        return os.getcwd().replace('\\', '/')
    
    def _permicao(self, caminho, permicao):
        """ define permissao para pasta """
        self.os_use.chmod(caminho, permicao)
    
    
    
    def path_to_folder(self, caminho='', counterSlashes=False):
        """ diz o caminho para a pasta (padrão é o caminho main.py) """
        
        if counterSlashes:
            return f'{self.__current_path()}{caminho}'.replace('/', '\\')
        else:
            return f'{self.__current_path()}{caminho}'
    
    def salvar_arquivo(self, caminho: str, nome_arquivo: str, counterSlashes=False):
        """ Salva arquivo com o caminho e nome e qual barra """
        
        if counterSlashes:
            return f'{self.path_to_folder(caminho=caminho)}/{nome_arquivo}'.replace('/', '\\')
        else:
            return f'{self.path_to_folder(caminho=caminho)}/{nome_arquivo}'
        
    def listarPasta(self, caminho: str):
        return self.os_use.listdir(caminho)

class WinAuto:
    def __init__(self):
        self.win_app = Application(backend='win32')
        super().__init__()
        
    def conectar_janela(self, nome_janela: str, timeout=4):
        self.win_app.connect(title= nome_janela, timeout= timeout)


class WinUse(Os_use, WinAuto):
    def __init__(self):
        self.autogui = pyautogui
        super().__init__()
        
    def pressKey(self, key : str, presses=1):
        """ Aperta uma tecla uma ou mais vezes """
        
        self.autogui.press(keys= key, presses= presses)
        
    def escrever(self, texto : str, intervalo = 0.05):
        """ Usa o teclado para escrever e com um intervalo """
        
        keyboard.write(texto, delay=intervalo)
        
    def moveToMiddle(self):
        """ Move o mouse para o centro da tela """
        
        self.autogui.moveTo(self.autogui.size().width/2, self.autogui.size().height/2)
        
    def click(self, button='left'):
        """ Faz um click com o mouse (padrão esquerdo) """
        
        self.autogui.click(button=button)