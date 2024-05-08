from window import *
import os
import getpass


"""
Adds a PATH environment variable to '/home/<USER>/.custom_env'
which gets called by '/home/<USER>/.bashrc"
@:param root: the tkinter main instance
"""
class PathAdder():
    def __init__(self, root):
        self.root = root
        self.draw()

    def delete(self):
        self.frame_wrapper.destroy()

    def draw(self):
        self.frame_wrapper = Frame(self.root)
        self.frame_wrapper.pack(side=TOP, fill=X)
        frame_entry = Frame(self.frame_wrapper)
        frame_entry.pack(side=TOP, pady=30)

        Label(frame_entry, text="Path:").pack(side=LEFT)
        self.entry_path = Entry(frame_entry)
        self.entry_path.select_range(0, END)
        self.entry_path.pack(side=LEFT)

        self.label_status = Label(self.frame_wrapper)
        self.label_status.pack(side=TOP, fill=X)
        btn_submit = Button(self.frame_wrapper, text="Submit", command=lambda: self.add_path())
        btn_submit.pack(side=TOP)

    # addds environment variable in '/home/USERNAME/.custom_path_vars'
    def add_path(self) -> None: # e.g. /home/hyperion/tests
        # nested function to change status label
        def set_label(status) -> None:
            match status:
                case STAT.OK:
                    self.label_status["bg"] = "green"
                    self.label_status["text"] = "Path has been added."
                case STAT.FAIL:
                    self.label_status["bg"] = "red"
                    self.label_status["text"] = "Error: Path does not exist!"

        # if path does not exist: print error msg
        path = self.entry_path.get()
        if not os.path.exists(path):
            set_label(STAT.FAIL)
            return

        # handle possible privilege errors
        try:
            username = getpass.getuser()
            custom_paths = f"/home/{username}/.custom_path_vars"
            # if .custom_path_vars does not exist: create file + append new path to PATH
            if not os.path.exists(custom_paths):
                with open(custom_paths, "w") as file:
                    file.write("#!/bin/bash\n")
                    file.write(f"export PATH=$PATH:{path}\n")
                with open(f"/home/{username}/.bashrc", "a") as file:
                    file.write(f"\n\n# Custom PATH amendments (created by {TITLE}):\n")
                    file.write("bash .custom_path_vars\n")
                set_label(STAT.OK)
            else:
                with open(custom_paths, "a") as file:
                    file.write(f"export PATH=$PATH:{path}\n")
                    set_label(STAT.OK)
        except PermissionError:
            self.label_status["bg"] = "red"
            self.label_status["text"] = "Error: Superuser permissions needed!!"
