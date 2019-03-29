"""Main page for the email application."""
import tkinter as tk
from datetime import datetime


class MainPage(tk.Frame):
    """Main page for application."""

    def __init__(self, parent):
        """Initialise Home Page class."""
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1000)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        """Create the pages widgets."""
        # Title
        time = str(datetime.now())
        msg = 'Good morning' if int(time[11:13]) < 12 else 'Good evening'
        print(self.parent.CURRENT_USER)
        name = self.parent.CURRENT_USER
        print(name)
        self.title = tk.Label(self,
                              text=f"{msg}, {name}",
                              font=("Helvetica", 24, "bold")
                              )
        self.title.grid()
