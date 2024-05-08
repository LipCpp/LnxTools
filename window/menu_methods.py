from window import *


"""
Methods for the menu bar
"""
class MenuMethods():
    @staticmethod
    def menu_about() -> None:
        L_TEXT = "LnxTools - About"
        child: Tk = Tk()
        child.title(L_TEXT)
        child.geometry("400x200")

        wrapper = Frame(child)
        wrapper.pack(side=TOP, fill=BOTH)
        Label(wrapper, text="LnxTools", font=15).pack()
        Label(wrapper, text="Free to use, open source software", font=10).pack()
        Label(wrapper, text="License: NONE", font=10).pack()

        child.mainloop()

