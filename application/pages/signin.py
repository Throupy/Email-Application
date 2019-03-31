"""Sign in page for the email application."""
import winsound
import tkinter as tk
from tkinter import messagebox
from pages.mainpage import MainPage


class SignIn(tk.Frame):
    """Landing page for application."""

    def __init__(self, parent):
        """Initialise Home Page class."""
        super().__init__(parent)
        self.parent = parent
        self.parent.grid_columnconfigure(0, weight=1000)
        self.create_widgets()

    def create_widgets(self):
        """Create the pages widgets."""
        # Title
        self.title = tk.Label(self,
                              text="Sign In",
                              font=("Helvetica", 24, "bold")
                              )
        self.title.grid()
        # Username label and entry
        self.usernameLabel = tk.Label(self,
                                      text="Username:",
                                      font=("Helvetica", 18)
                                      )
        self.usernameLabel.grid(pady=(50, 0))
        self.usernameEntry = tk.Entry(self)
        self.usernameEntry.grid(pady=(5, 0))
        # Password label and entry
        self.passwordLabel = tk.Label(self,
                                      text="Password:",
                                      font=("Helvetica", 18)
                                      )
        self.passwordLabel.grid(pady=(20, 0))
        self.passwordEntry = tk.Entry(self, show="*")
        self.passwordEntry.grid(pady=(5, 0))
        # Log in button
        self.loginButton = tk.Button(self,
                                     text=f"{' '*12}Log in{' '*12}",
                                     command=self.handleLogin)
        self.loginButton.grid(pady=(20, 0))
        # Register button
        self.loginButton = tk.Button(self,
                                     text=f"{' '*11}Register{' '*11}",
                                     command=self.handleRegister)
        self.loginButton.grid()

    def handleLogin(self):
        """Handle the login event."""
        if self.parent.dbhelper.userExists(self.usernameEntry.get()):
            # login
            self.parent.CURRENT_USER = self.usernameEntry.get()
            winsound.PlaySound("SystemExclamation", winsound.SND_ASYNC)
            # I need to add the page here, otherwise it gets initialized at the
            # start, so the CURRENT_USER isn't set, thus is None.
            self.parent.pages[MainPage] = MainPage(self.parent)
            self.parent.change_page(MainPage)
        else:
            messagebox.showinfo("Oops", "No user was found with those details")

    def handleRegister(self):
        """Handle the register event."""
        if len(self.usernameEntry.get()) > 0 and \
           len(self.passwordEntry.get()) > 0:
            confirmation = messagebox.askyesno("Confirmation",
            f"Do you want to add a user with name {self.usernameEntry.get()}?")
            if confirmation:
                self.parent.dbhelper.createUser(self.usernameEntry.get(),
                                                self.passwordEntry.get())
                return True
            return False
        else:
            messagebox.showerror("Oops", "You must populate all fields")
