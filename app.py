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
    def __init__(self, master, **kwargs):
          super().__init__(master, **kwargs)
          self._nav_ui()

    def _nav_ui(self):
        self.card = ctk.CTkFrame(self, fg_color="black")
        self.card.grid(row=0, column=0, sticky='ew')
        self.grid_columnconfigure(0, weight=1)
        
        
        self.dash_btn = ctk.CTkButton(self.card, text="Dashboard")
        self.dash_btn.grid(row=0, column=0, padx=10, pady=10)
        self.pro_btn = ctk.CTkButton(self.card, text="Profile")
        self.pro_btn.grid(row=0, column=1, padx=10, pady=10)
        self.task_btn = ctk.CTkButton(self.card, text="Tasks")
        self.task_btn.grid(row=0, column=2, padx=10, pady=10)
        self.que_btn = ctk.CTkButton(self.card, text="Quests")
        self.que_btn.grid(row=0, column=3, padx=10, pady=10)
        self.work_btn = ctk.CTkButton(self.card, text="Work")
        self.work_btn.grid(row=0, column=4, padx=10, pady=10)
        self.bank_btn = ctk.CTkButton(self.card, text="Bank")
        self.bank_btn.grid(row=0, column=5, padx=10, pady=10)
        self.upd_btn = ctk.CTkButton(self.card, text="Updates")
        self.upd_btn.grid(row=0, column=6, padx=10, pady=10)
          

         
         
         
         
class Dashboard(ctk.CTkFrame):
     def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         
         self.grid_columnconfigure(0, weight = 1)
         self.grid_columnconfigure(1, weight = 1)
         self.grid_rowconfigure(1, weight = 1)
         self.grid_rowconfigure(2, weight = 1)
         
         navbar(self).grid(row=0, column=0, sticky = 'nwe', columnspan=2, padx=5)
         
         self.card1 = ctk.CTkFrame(self, fg_color="white")
         self.card1.grid(row=1, column=0, padx=10, pady=10, sticky = 'nwes')
        
         self.card2 = ctk.CTkFrame(self, fg_color="white")
         self.card2.grid(row=1, column=1, padx=10, pady=10, sticky = 'nwes')
        
         self.card3 = ctk.CTkFrame(self, fg_color="white")
         self.card3.grid(row=2, column=0, padx=10, pady=10, sticky = 'nwes')
        
         self.card4 = ctk.CTkFrame(self, fg_color="white")
         self.card4.grid(row=2, column=1, padx=10, pady=10, sticky = 'nwes')
         
         

class Profile(ctk.CTkFrame):
     def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         navbar(self).grid(row=0, column=0)
         
         label = ctk.CTkLabel(self, text="Welcome to Dashboard!")
         label.grid(row=1, column=0)
         
class Tasks(ctk.CTkFrame):
     def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         navbar(self).grid(row=0, column=0)
         
         label = ctk.CTkLabel(self, text="Welcome to Dashboard!")
         label.grid(row=1, column=0)
         
         
class Quests(ctk.CTkFrame):
     def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         navbar(self).grid(row=0, column=0)
         
         label = ctk.CTkLabel(self, text="Welcome to Dashboard!")
         label.grid(row=1, column=0)
         
class Work(ctk.CTkFrame):
     def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         navbar(self).grid(row=0, column=0)
         
         label = ctk.CTkLabel(self, text="Welcome to Dashboard!")
         label.grid(row=1, column=0)
         
class Bank(ctk.CTkFrame):
     def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         navbar(self).grid(row=0, column=0)
         
         label = ctk.CTkLabel(self, text="Welcome to Dashboard!")
         label.grid(row=1, column=0)
         
class Updates(ctk.CTkFrame):
     def __init__(self, master, **kwargs):
         super().__init__(master, **kwargs)
         navbar(self).grid(row=0, column=0)
         
         label = ctk.CTkLabel(self, text="Welcome to Dashboard!")
         label.grid(row=1, column=0)
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
          page_class(self).pack(fill="both", expand=True)

if __name__ == "__main__":
      app = App()
      app.mainloop()

