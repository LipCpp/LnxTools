from tkinter import *
import window

def main():
    window.Window(root=Tk())

if __name__ == '__main__':
    # main()
    import window.path_adder
    window.path_adder.PathAdder.add_path('awsd')