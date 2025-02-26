import pyautogui
import pywinauto

class AutoGUI:
    def __init__(self):
        self.autogui = pyautogui
        
    def pressKey(self, key, presses=0):
        self.autogui.press(key, presses)
        
    def moveToMiddle(self):
        self.autogui.moveTo(self.autogui.size().width/2, self.autogui.size().height/2)