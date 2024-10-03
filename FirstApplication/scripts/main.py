import tkinter as tk
import ctypes
from tkinter import ttk
from PIL import Image, ImageTk

class App:
    def __init__(self):
        # Initializing the main window
        self.root = tk.Tk()
        
        # Using ctypes to entrust a Windows icon
        myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
        # Setting window title and size
        # self.root is the window application
        self.root.geometry('350x200')
        self.root.title("FirstApp")
        
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)
        
        self.text = ttk.Label(self.mainframe, text="Hello World", font=('impact', 30), background='white')
        self.text.grid(row=0, column=0)
        
        
        # Setting the icon in the top right corner
        icon_path = 'FirstApplication\\images\\dice_icon.jpg'
        icon_path_ico = 'FirstApplication\\images\\dice_icon.ico'
        icon = Image.open(icon_path)
        photo = ImageTk.PhotoImage(icon)
        self.root.wm_iconphoto(False, photo)
        self.root.iconbitmap(default=icon_path_ico)
        
             
        
        # Main loop is run at the end so GUI is displayed
        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0)
        self.root.mainloop()
        return
    
if __name__ == "__main__":
    App()
