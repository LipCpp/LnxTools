import os

from window import *
from tkinter import ttk


"""
adds a .desktop file in /usr/share/applications
@:param root: the tkinter main instance
"""
class ApplicationAdder():
    def __init__(self, root):
        self.root = root
        self.draw()

    def delete(self) -> None:
        self.frame_wrapper.destroy()
        self.frame_submit.destroy()

    def draw(self) -> None:
        PADDING = 0.5
        self.frame_wrapper = Frame(self.root)
        frame_labels = Frame(self.frame_wrapper)
        frame_div = Frame(self.frame_wrapper, width=5)
        frame_entries = Frame(self.frame_wrapper)

        # Label(self.root, text="Add a .desktop file in /usr/share/applications to add an application to system").pack(side=TOP, pady=PADDING)

        Label(frame_labels, text="* Name:").pack(side=TOP, pady=PADDING)
        self.entry_name = Entry(frame_entries, width=MAX_WIDTH)
        self.entry_name.pack(side=TOP)

        Label(frame_labels, text="* Exec:").pack(side=TOP, pady=PADDING)
        self.entry_exec = Entry(frame_entries, width=MAX_WIDTH)
        self.entry_exec.pack(side=TOP)

        Label(frame_labels, text="* Terminal:").pack(side=TOP, pady=PADDING)
        terminal = StringVar()
        self.combo_terminal = ttk.Combobox(frame_entries,
                                           textvariable=terminal,
                                           values=("true", "false"),
                                           width=MAX_WIDTH)
        self.combo_terminal.pack(side=TOP)

        Frame(frame_labels, height=3).pack(side=TOP)
        Label(frame_labels, text="Version:").pack(side=TOP, pady=PADDING)
        self.entry_version = Entry(frame_entries, width=MAX_WIDTH)
        self.entry_version.pack(side=TOP)

        Label(frame_labels, text="Comment:").pack(side=TOP, pady=PADDING)
        self.entry_comment = Entry(frame_entries, width=MAX_WIDTH)
        self.entry_comment.pack(side=TOP)

        Label(frame_labels, text="GenericName:").pack(side=TOP, pady=PADDING)
        self.entry_genname = Entry(frame_entries, width=MAX_WIDTH)
        self.entry_genname.pack(side=TOP)

        Label(frame_labels, text="Keywords:").pack(side=TOP, pady=PADDING)
        self.entry_keywords = Entry(frame_entries, width=MAX_WIDTH)
        self.entry_keywords.pack(side=TOP)

        Label(frame_labels, text="Icon:").pack(side=TOP, pady=PADDING)
        self.entry_icon = Entry(frame_entries, width=MAX_WIDTH)
        self.entry_icon.pack(side=TOP)

        self.frame_wrapper.pack(side=TOP, fill=BOTH)
        frame_labels.pack(side=LEFT, fill=BOTH)
        frame_div.pack(side=LEFT, fill=BOTH)
        frame_entries.pack(side=LEFT, fill=BOTH)

        # error message bar and submit button
        self.frame_submit = Frame(self.root)
        self.label_error = Label(self.frame_submit, fg="white")
        self.label_error.pack(side=TOP, fill=X)
        Button(self.frame_submit, text="Generate File", command=lambda: self.btn_submit()).pack(side=TOP)
        self.frame_submit.pack(side=TOP, fill=BOTH, pady=15)

    def btn_submit(self) -> None:
        version = self.entry_version.get()
        name = self.entry_name.get()
        comment = self.entry_comment.get()
        genname = self.entry_genname.get()
        keywords = self.entry_keywords.get()
        execute = self.entry_exec.get()
        icon = self.entry_icon.get()
        terminal = self.combo_terminal.get()

        # error handling
        self.label_error["bg"] = "green"
        self.label_error["text"] = f"Successfully created {name}.desktop"
        if terminal == "":
            self.label_error["bg"] = "red"
            self.label_error["text"] = "Error: Terminal mode not specified!"
            return
        elif terminal != "true" and terminal != "false":
            self.label_error["bg"] = "red"
            self.label_error["text"] = "Error: Terminal mode ('true' or 'false') not specified!"
            return
        if execute == "":
            self.label_error["bg"] = "red"
            self.label_error["text"] = "Error: Executable not specified!"
            return
        if name == "":
            self.label_error["bg"] = "red"
            self.label_error["text"] = "Error: Name not specified!"
            return

        # .desktop file template
        data = f"""
[Desktop Entry]
Type=Application
X-MultipleArgs=false
Version={version}
Name={name}
Comment={comment}
GenericName={genname}
Keywords={keywords}
Exec={execute}
Terminal={terminal}
Icon={icon}
"""
        # write .desktop file
        # TODO: enable root privileges at runtime
        try:
            with open(f"/usr/share/applications/{name}.desktop", "w") as file:
                file.write(data)
        except PermissionError as e:
            self.label_error["bg"] = "red"
            self.label_error["text"] = "Error: Program needs root (sudo) permissions!"

