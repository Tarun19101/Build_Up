import customtkinter as ctk
import database
import functions

ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")


class RegisterPage(ctk.CTkFrame):
      def __init__(self, master, **kwargs):
          super().__init__(master, **kwargs)

          # Main container centered on screen
          self.outer_container = ctk.CTkFrame(self, fg_color="red")
          self.outer_container.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.3, relheight=0.6)
          
          self.inner_container = ctk.CTkFrame(self.outer_container, fg_color="black")
          self.inner_container.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.98, relheight=0.98)
            
          self.inner_container.grid_columnconfigure(1, weight = 2)


          # Title
          self.title_label = ctk.CTkLabel(
              self.inner_container,
              text="Create Account",
              font=ctk.CTkFont(size=28, weight="bold")
          )
          self.title_label.grid(row=0, column=0, padx=10, pady=20, columnspan=2)

          # Username field
          self.username_label = ctk.CTkLabel(self.inner_container, text="Username:")
          self.username_label.grid(row=1, column=0, pady=20, padx=10)
          self.username_entry = ctk.CTkEntry(self.inner_container, placeholder_text="Enter username")
          self.username_entry.grid(row=1, column=1, pady=20, padx=10)

          # DOB field
          self.dob_label = ctk.CTkLabel(self.inner_container, text="Date of birth (DOB):")
          self.dob_label.grid(row=2, column=0, pady=20, padx=10)
          self.dob_entry = ctk.CTkEntry(self.inner_container, placeholder_text="DD-MM-YYYY")
          self.dob_entry.grid(row=2, column=1, pady=20, padx=10)
          
         
          # Submit button
          self.submit_btn = ctk.CTkButton(
              self.inner_container,
              text="Register",
              command=self.register
          )
          self.submit_btn.grid(row=3, column=0, padx=10, pady=20, columnspan=2)

      def register(self):
          name = self.username_entry.get()
          dob_date = self.dob_entry.get()
          dob = functions.convert_date_format(dob_date)

          database.register_user(name, dob)
          for widget in self.winfo_children():
              widget.destroy()
          Dashboard(self).pack(fill="both", expand=True)
          
class navbar(ctk.CTkFrame):
                    
    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.card = ctk.CTkFrame(self, fg_color="black")
        self.card.grid(row=0, column=0, sticky='ew')
        self.grid_columnconfigure(0, weight=1)
        
        self.dash_btn = ctk.CTkButton(self.card, text="Dashboard", command=lambda: self.app.show_page(Dashboard))
        self.dash_btn.grid(row=0, column=0, padx=10, pady=10)
        self.pro_btn = ctk.CTkButton(self.card, text="Profile", command=lambda: self.app.show_page(Profile))
        self.pro_btn.grid(row=0, column=1, padx=10, pady=10)
        self.task_btn = ctk.CTkButton(self.card, text="Tasks", command=lambda: self.app.show_page(Tasks))
        self.task_btn.grid(row=0, column=2, padx=10, pady=10)
        self.que_btn = ctk.CTkButton(self.card, text="Quests", command=lambda: self.app.show_page(Quests))
        self.que_btn.grid(row=0, column=3, padx=10, pady=10)
        self.work_btn = ctk.CTkButton(self.card, text="Work", command=lambda: self.app.show_page(Work))
        self.work_btn.grid(row=0, column=4, padx=10, pady=10)
        self.bank_btn = ctk.CTkButton(self.card, text="Bank", command=lambda: self.app.show_page(Bank))
        self.bank_btn.grid(row=0, column=5, padx=10, pady=10)
        self.upd_btn = ctk.CTkButton(self.card, text="Updates", command=lambda: self.app.show_page(Updates))
        self.upd_btn.grid(row=0, column=6, padx=10, pady=10)
        

         
        
          

class Base_layout(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         self.app = self.winfo_toplevel()
         
         self.grid_columnconfigure(0, weight = 1)
         self.grid_columnconfigure(1, weight = 1)
         self.grid_rowconfigure(1, weight = 1)
         self.grid_rowconfigure(2, weight = 1)
         
         menu = navbar(self, self.app)
         menu.grid(row=0, column=0, sticky = 'new', columnspan=2, padx=5)
         
         colors = ["red","blue","green","yellow"]
         
         for i,color in enumerate(colors, 1):
            card = ctk.CTkFrame(self, fg_color=color)
            card.grid(row=(1 if i<=2 else 2), column=(0 if i in [1,3] else 1), padx=10, pady=10, sticky = 'news')
            inner = ctk.CTkFrame(card, fg_color="white")
            inner.grid(row=0, column=0, padx=5, pady=5, sticky = 'news')
            
            card.grid_columnconfigure(0, weight = 1)
            card.grid_rowconfigure(0, weight = 1)
            
            setattr(self, f"card{i}", card)
            setattr(self, f"inner_card{i}", inner)
            
    def refresh_data(self):
        pass
             
         
         
class Dashboard(Base_layout):
    def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         ctk.CTkLabel(self.inner_card1, text="Dashboard Content", fg_color='black').pack(padx=10, pady=10)

         
    def refresh_data(self):
        pass
         
         

class Profile(Base_layout):
    def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         ctk.CTkLabel(self.inner_card1, text="Profile Content", fg_color='black').pack(padx=10, pady=10)

         
    def refresh_data(self):
        pass
         
        
         
class Tasks(Base_layout):
    def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         ctk.CTkLabel(self.inner_card1, text="Tasks Content", fg_color='black').pack(padx=10, pady=10)

         
    def refresh_data(self):
        pass
         
         
class Quests(Base_layout):
    def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         ctk.CTkLabel(self.inner_card1, text="Quests Content", fg_color='black').pack(padx=10, pady=10)

         
    def refresh_data(self):
        pass
         
class Work(Base_layout):
    def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         ctk.CTkLabel(self.inner_card1, text="Work Content", fg_color='black').pack(padx=10, pady=10)

         
    def refresh_data(self):
        pass
         
class Bank(Base_layout):
    def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         ctk.CTkLabel(self.inner_card1, text="Bank Content", fg_color='black').pack(padx=10, pady=10)

         
    def refresh_data(self):
        pass
         
class Updates(Base_layout):
    def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         ctk.CTkLabel(self.inner_card1, text="Updates Content", fg_color='black').pack(padx=10, pady=10)

         
    def refresh_data(self):
        pass
         
         
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Build Up")
        self.geometry("1920x1080")

        database.create_tables()
        see_user = database.check_user()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.pages = {}
        for PageClass in [Dashboard, Profile, Tasks, Quests, Work, Bank, Updates]:
            page = PageClass(self)
            page.grid(row=0, column=0, sticky="nsew")
            self.pages[PageClass] = page
            
        self.show_page(Dashboard if see_user else RegisterPage)
    
    def show_page(self, page_class):
        if page_class == RegisterPage:
            for widget in self.winfo_childern():
                widget.destroy()
            RegisterPage(self).pack(fill="both", expand=True)
        else:
            self.pages[page_class].tkraise()
            if hasattr(self.pages[page_class], 'refresh_data'):
                self.pages[page_class].refresh_data()

if __name__ == "__main__":
      app = App()
      app.mainloop()

