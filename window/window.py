from window import *
from window.menu_methods import MenuMethods
from window.function_select import FunctionSelect


"""
initializes the tkinter window instance
@:param root: Tk() object
"""
class Window():
    def __init__(self, root):
        HEIGHT = 300
        WIDTH = 450
        self.root: Tk = root
        self.root.title(TITLE)
        self.root.geometry(f"{str(WIDTH)}x{str(HEIGHT)}")
        # self.root.configure(bg="#000020")

        # configure menu bar
        menubar = Menu()

        menubar.add_command(label="About", command=MenuMethods.menu_about)
        self.root.config(menu=menubar)

        FunctionSelect(self.root)

        self.root.mainloop()
