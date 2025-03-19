import curses
import time

class Curses:
    def __init__(self, options=None):
        self.options = options
        self.indice = 0
        
        stdscr = curses.initscr()
        curses.start_color()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        
        self.inpt = stdscr
        
    def opcoes(self, header_text = '', haveCancel = False):
        if haveCancel == True:
            self.options.append({"desc":"cancelar", "value": len(self.options) + 1})
        
        curses.curs_set(0)
        inpt = self.inpt
        inpt.nodelay(False)
        inpt.timeout(100)
        
        while True:
            inpt.clear()
            
            if header_text == '':
                inpt.addstr(0, 0, "Use ↑ ↓ para navegar e Enter para selecionar\n", curses.A_BOLD)
            else:
                inpt.addstr(0, 0, header_text, curses.A_BOLD)
            
            for i, opcao in enumerate(self.options):
                if i == self.indice:
                    if haveCancel == True:
                        inpt.addstr(i + 2, 0, f" > {opcao['desc']}", curses.A_BOLD | curses.color_pair(1)) if opcao['desc'] != "cancelar" else inpt.addstr(i + 2, 0, f"-- {opcao['desc']} --", curses.A_BOLD | curses.color_pair(3))
                    else:
                        inpt.addstr(i + 2, 0, f" > {opcao['desc']}", curses.A_BOLD | curses.color_pair(1))

                elif haveCancel == True and opcao['desc'] == "cancelar":
                    inpt.addstr(i + 2, 0, f"-- {opcao['desc']} --", curses.color_pair(2))
                    
                else:
                    inpt.addstr(i + 2, 0, f" {opcao['desc']}")

            tecla = inpt.getch()
            
            if tecla == curses.KEY_UP:
                self.indice = (self.indice - 1) % len(self.options)
            elif tecla == curses.KEY_DOWN:
                self.indice = (self.indice + 1) % len(self.options)
            elif tecla == 10:
                curses.endwin()
                return self.options[self.indice]['value']
            
    def setString(self, strg, positionX = 0, positionY = 0):
        curses.curs_set(0)
        inpt = self.inpt
        inpt.clear()
        inpt.nodelay(False)
        inpt.timeout(100)
        inpt.addstr(positionY, positionX, strg)
        inpt.refresh()
        time.sleep(1.2)