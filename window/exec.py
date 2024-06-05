import os
import getpass

def add_path(path):
    username = getpass.getuser()
    custom_paths = f"/home/{username}/.custom_path_vars"

    # if .custom_path_vars does not exist: create file + append new path to PATH
    if not os.path.exists(custom_paths):
        with open(custom_paths, "w") as file:
            file.write("#!/bin/bash\n")
            file.write(f"export PATH=$PATH:{path}\n")
        with open(f"/home/{username}/.bashrc", "a") as file:
            file.write(f"\n\n# Custom PATH amendments:\n")
            file.write("bash .custom_path_vars\n")
    else:
        with open(custom_paths, "a") as file:
            file.write(f"export PATH=$PATH:{path}\n")


def add_desktop_file(version, name, comment, genname, keywords, execute, terminal, icon):
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
        print('[ERROR] :: Root privileges required!')
