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
          
 
 
class Dashboard(ctk.CTkFrame):
      def __init__(self, master, **kwargs):
          super().__init__(master, **kwargs)
          label = ctk.CTkLabel(self, text="Welcome to Dashboard!")
          label.place(relx=0.5, rely=0.5, anchor="center")

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

