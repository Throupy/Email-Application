"""Main application frame."""
import tkinter as tk
from .signin import SignIn
from .mainpage import MainPage
from backend.DBHelper import DBHelper


class Application(tk.Tk):
    """Main Application class inheriting from tkinter.Tk."""

    CURRENT_USER = None

    def __init__(self):
        """Initialise Application class."""
        super().__init__()
        self.dbhelper = DBHelper()
        self.grid_columnconfigure(0, weight=1000)

        self.resizable(False, False)
        self.geometry("500x500")
        self.pages = {}
        self.create_pages()

    def create_pages(self):
        """Create the applications pages."""
        self.pages[SignIn] = SignIn(self)
        self.change_page(SignIn)

    def change_page(self, new_page):
        """
        Change the currently displayed page.

        Arguments:
            new_page - The page to change to
        """
        for page in self.grid_slaves():
            page.grid_remove()
        self.pages[new_page].grid(column=0, row=0)
        self.CURRENT_USER = self.CURRENT_USER
