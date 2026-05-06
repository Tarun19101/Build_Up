import customtkinter as ctk
import database
import functions


ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")
        

class RegisterPage(ctk.CTkFrame):
    def __init__(self, master : "App", **kwargs):
        super().__init__(master, **kwargs)
        
        
        
        
        
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Build Up")
        self.geometry("1920x1080")
        
        
        
        
        
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
