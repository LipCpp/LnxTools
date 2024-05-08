from window import *
from window.path_adder import PathAdder
from window.application_adder import ApplicationAdder

"""
Used to select wanted functionality
@:param root: the tkinter main instance
@:param mode: the current functionality
    which is shown on the right side of FunctionSelect
"""


class FunctionSelect():
    def __init__(self, root):
        self.root: Tk = root
        self.div_func_sel()
        # currently displayed functionality on right side of the window:
        self.curr_displayed = ApplicationAdder(self.root)

    def switch_mode(self, new_mode) -> None:
        self.curr_displayed.delete()
        match new_mode.get():
            case 0:
                self.curr_displayed = ApplicationAdder(self.root)
            case 1:
                self.curr_displayed = PathAdder(self.root)

    def div_func_sel(self) -> None:
        frame_wrapper = Frame(self.root, bg=THEME_SEC)

        values = {
            "Application Adder": 0,     # 0 means selected=white (due to contrast)
            "Path Adder": 1,
        }

        mode = IntVar()
        for (text, value) in values.items():
            Radiobutton(frame_wrapper,
                        text=text,
                        value=value,
                        variable=mode,
                        bg=THEME_SEC,
                        command=lambda: self.switch_mode(mode),
                        indicatoron=False).pack(side=TOP, fill=X)

        frame_wrapper.pack(side=LEFT, fill=Y)
