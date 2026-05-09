import customtkinter as ctk
import database
import functions


ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")
        

class RegisterPage(ctk.CTkFrame):
    def __init__(self, master : "App", **kwargs):
        super().__init__(master, **kwargs)
        
        l1 = ctk.CTkLabel(self, text="Hello")
        l1.grid(row=0,column=0)
        
        
        
class Dashboard(ctk.CTkFrame):
    def __init__(self, master : "App", **kwargs):
        super().__init__(master, **kwargs)
        
        
        
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Build Up")
        self.geometry("1920x1080")
        
        database.create_tables()
        see_user = database.check_user()
        
        self._page(see_user)

        
    def _page(self, see_user):
        if see_user:
            self.show_page(Dashboard)
        else:
            self.show_page(RegisterPage)
                
    def show_page(self, page_class):

        for widget in self.winfo_children():
            widget.destroy()
                
        page_class(self).grid(row=0,column=0)
        
        
        
        
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
