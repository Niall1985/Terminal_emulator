import os
import sys
import tkinter as tk
from tkinter import scrolledtext

# Command functions
def ls(path):
    try:
        dir_list = os.listdir(path)
        return f"The list of directories in {path} are:\n" + "\n".join(dir_list)
    except Exception as e:
        return str(e)

def pwd():
    try:
        current_dir = os.getcwd()
        return f"The current directory is:\n{current_dir}"
    except Exception as e:
        return str(e)

def mkdir(path):
    try:
        os.mkdir(path)
        return "Directory has been created"
    except Exception as e:
        return str(e)

def cd(path):
    try:
        os.chdir(path)
        return f"Directory has been changed to {os.getcwd()}"
    except Exception as e:
        return str(e)
    
# def rmdir(path):
#     try:
#         os.rmdir(path)
#         return f"Directory has been deleted"
#     except Exception as e:
#         return str(e)

def clear_terminal():
    return ""

def quit_app():
    sys.exit(0)

# Terminal Application
class TerminalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Terminal Emulator")
        self.configure(bg="#2E2E2E")
        self.geometry("800x600")

        self.output_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, bg="#1E1E1E", fg="#FFFFFF", insertbackground="#FFFFFF", font=("Courier", 12))
        self.output_area.pack(expand=True, fill=tk.BOTH)
        self.output_area.bind("<Return>", self.execute_command)
        self.output_area.bind("<BackSpace>", self.handle_backspace)
        self.output_area.bind("<Key>", self.handle_key)

        self.insert_prompt()

    def insert_prompt(self):
        current_dir = os.getcwd()
        self.output_area.insert(tk.END, f"\n{current_dir} $@ ", "dir")
        self.output_area.mark_set(tk.INSERT, tk.END)
        self.output_area.tag_config("dir", foreground="#FF0000")
        self.output_area.tag_config("command", foreground="#FFFF00")
        self.output_area.tag_config("output", foreground="#FFFFFF")
        self.output_area.tag_add("dir", "end-1c linestart", "end-1c")
        self.output_area.mark_gravity(tk.INSERT, tk.RIGHT)
        self.output_area.focus()

    def execute_command(self, event):
        self.output_area.config(state=tk.NORMAL)
        command_text = self.get_current_command()
        self.output_area.insert(tk.END, "\n", "output")

        if command_text.startswith("ls"):
            path = command_text[3:] if len(command_text) > 2 else os.getcwd()
            output = ls(path.strip())
        elif command_text == "pwd":
            output = pwd()
        elif command_text.startswith("mkdir"):
            path = command_text[6:]
            output = mkdir(path.strip())
        elif command_text.startswith("cd"):
            path = command_text[3:]
            output = cd(path.strip())
        elif command_text == "clear":
            self.clear_output()
            return
        elif command_text == ":q!":
            quit_app()
        else:
            output = "Command not found: " + command_text

        self.output_area.insert(tk.END, f"{output}\n", "output")
        if command_text.startswith("cd"):
            self.insert_prompt()
        else:
            self.output_area.insert(tk.END, f"\n{os.getcwd()} $@ ", "dir")
            self.output_area.tag_add("dir", "end-1c linestart", "end-1c")

        self.output_area.mark_set(tk.INSERT, tk.END)
        self.output_area.see(tk.END)

    def get_current_command(self):
        command = self.output_area.get("end-1c linestart", "end-1c").split("$@ ")[-1]
        return command.strip()

    def handle_backspace(self, event):
        current_line = self.output_area.get("end-1c linestart", "end-1c")
        if current_line.endswith("$@ "):
            return "break"
        else:
            return None

    def handle_key(self, event):
        current_line = self.output_area.get("end-1c linestart", "end-1c")
        if current_line.endswith("$@ "):
            self.output_area.tag_add("command", "end-1c linestart+4c", "end-1c")

    def clear_output(self):
        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete(1.0, tk.END)
        self.insert_prompt()
        self.output_area.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = TerminalApp()
    app.mainloop()
