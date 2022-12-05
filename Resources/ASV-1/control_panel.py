# control_panel.py
from tkinter import Frame, Button, Menu

class ControlPanel(Frame):

    def __init__(self, master, **options):
        Frame.__init__(self, master, **options)
        self.grid(row=0, column=1)
        self.config(padx=5, pady=5)

        b_advance = Button(self, text="Advance", command=master.advance)
        b_advance.pack(padx=5, pady=5, side='top')

        b_reset = Button(self, text="Reset", command=master.reset)
        b_reset.pack(padx=5, pady=5, side='top')

        self.menu = Menu(master)
        file_menu = Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Load map...", command=master.load_map_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=master.quit)
        self.menu.add_cascade(label="File", menu=file_menu)
