import tkinter as tk
import ctypes
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Menu
from setup import Setup
from simulation import Simulation

class App:
    def __init__(self):
        # Initializing the main window
        self.root = tk.Tk()
        
        # Adding a menu bar
        # menubar = Menu(self.root)
        # filemenu = Menu(menubar, tearoff=0)
        # menubar.add_cascade(label="File", menu=filemenu)
        # filemenu.add_command(label="New File", command=None)
        # filemenu.add_command(label="Open...", command=None)
        # filemenu.add_command(label="Save", command=None)
        # filemenu.add_separator()
        # filemenu.add_command(label="Exit", command=self.root.destroy)        
        
        # edit = Menu(menubar, tearoff=0)
        # menubar.add_cascade(label="Edit", menu=edit)
        # edit.add_command(label="Cut", command=None)
        # edit.add_command(label="Copy", command=None)
        # edit.add_command(label="Paste", command=None)
        # edit.add_separator()
        # edit.add_command(label="Find...", command=None) 
        
        
        
        # Using ctypes to entrust a Windows icon
        myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
        # Setting window title and size
        # self.root is the window application btw
        screen_width, screen_height = Setup.get_monitor_size()        
        
        
        self.root.geometry(str(screen_width) + 'x' + str(screen_height))
        self.root.title("OMorse Tools v0.0.2")
        
        # Add to debug mode method
        # print(str(screen_width) + "x" + str(screen_height))
        
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)
        
        self.text = ttk.Label(self.mainframe, text="Hello World", font=('impact', 30), background='white')
        self.text.grid(row=2, column=0)
        
       
            
        
        
        # Setting the icon in the top right corner
        icon_path = 'FirstApplication\\images\\o_morse_logo_rounded.png'
        icon_path_ico = 'FirstApplication\\images\\o_morse_logo_rounded.ico'
        icon = Image.open(icon_path)
        photo = ImageTk.PhotoImage(icon)
        self.root.wm_iconphoto(False, photo)
        self.root.iconbitmap(default=icon_path_ico)
        
             
        
        # Main loop is run at the end so GUI is displayed
        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=3, column=0)
        # self.root.config(menu=menubar)
        self.root.mainloop()
        return
    
if __name__ == "__main__":
    App()
