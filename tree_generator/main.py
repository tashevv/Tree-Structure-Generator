#!/usr/bin/env python3

import os
import argparse
import sys


def generate_tree(root_path, prefix="", ignore=None, max_depth=None, current_depth=0):
    try:
        entries = sorted(os.listdir(root_path))
    except PermissionError:
        print(f"{prefix}└── [Permission Denied]")
        return

    if ignore:
        entries = [e for e in entries if e not in ignore]

    entries_count = len(entries)

    for i, entry in enumerate(entries):
        path = os.path.join(root_path, entry)
        connector = "└── " if i == entries_count - 1 else "├── "

        if os.path.isdir(path):
            print(f"{prefix}{connector}{entry}/")

            if max_depth is None or current_depth < max_depth:
                extension = "    " if i == entries_count - 1 else "│   "
                generate_tree(
                    path,
                    prefix + extension,
                    ignore,
                    max_depth,
                    current_depth + 1,
                )
        else:
            print(f"{prefix}{connector}{entry}")


def print_tree(root_path, ignore=None, max_depth=None):
    root_name = os.path.basename(os.path.abspath(root_path))
    print(f"{root_name}/")
    generate_tree(root_path, "", ignore, max_depth)


def main():
    import tkinter as tk
    from tkinter import filedialog

    # Hide the root window
    root = tk.Tk()
    root.withdraw()

    print("Select folder to generate tree structure... \n")

    # Open folder picker
    path = filedialog.askdirectory(title="Select a folder")

    if not path:
        print("No folder selected.")
        return

    print_tree(path)

    input("\nPress Enter to close...")
    main()

if __name__ == "__main__":
    main()