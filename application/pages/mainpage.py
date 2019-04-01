"""Main page for the email application."""
import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox
from datetime import datetime
from utils.mail import sendMail


class MainPage(tk.Frame):
    """Main page for application."""

    def __init__(self, parent):
        """Initialise Home Page class."""
        super().__init__(parent)
        self.parent = parent
        self.parent.grid_columnconfigure(0, weight=0)
        self.create_widgets()

    def create_widgets(self):
        """Create the pages widgets."""
        # Title
        time = str(datetime.now())
        msg = 'Good morning' if int(time[11:13]) < 12 else 'Good evening'
        # Top left
        self.userInfo = tk.PanedWindow(self, relief=tk.SUNKEN)
        self.username = tk.Label(self.userInfo,
                                 text=self.parent.CURRENT_USER,
                                 font=("Helvetica", 16, "bold"),
                                 borderwidth=4)
        self.username.grid()
        self.time = tk.Label(self.userInfo,
                             text=time[:11] + '\n' + time[12:19],
                             font=("Helvetica", 12))
        self.time.grid()
        self.userInfo.grid()
        # Top bar
        self.topBarPanedWindow = tk.PanedWindow(self,
                                                relief=tk.SUNKEN,
                                                borderwidth=3,
                                                )
        self.title = tk.Label(self.topBarPanedWindow,
                              text=f"{msg}, {self.parent.CURRENT_USER}",
                              font=("Helvetica", 24, "bold"),
                              height=2)
        self.title.grid(row=0, column=2)
        self.topBarPanedWindow.grid(row=0, column=2)
        # Buttons
        self.buttonPanedWindow = tk.PanedWindow(self,
                                                relief=tk.SUNKEN,
                                                borderwidth=3)
        self.sendMailButton = tk.Button(self.buttonPanedWindow,
                                        text="Send mail",
                                        width=12,
                                        height=3,
                                        command=self.handleSendMail)
        self.sendMailButton.grid(row=2, column=0, pady=(20, 0))
        self.logoutButton = tk.Button(self.buttonPanedWindow,
                                      text="Log out",
                                      width=12,
                                      height=3)
        self.logoutButton.grid(row=4, column=0, pady=(20, 0))
        self.buttonPanedWindow.grid()

        # Content frame
        self.contentFrame = tk.Frame(self)

    def handleSendMail(self):
        """Handle event of send mail button."""
        self.clearContent()

        self.senderLabel = tk.Label(self.contentFrame,
                                    text="    Sender email address")
        self.senderLabel.grid(row=1, column=2, sticky=tk.W)
        self.senderEntry = tk.Entry(self.contentFrame, width=25)
        self.senderEntry.grid(row=1, column=3, sticky=tk.W)

        self.senderPasswordLabel = tk.Label(self.contentFrame,
                                            text="    Sender password")
        self.senderPasswordLabel.grid(row=2, column=2, sticky=tk.W)
        self.senderPasswordEntry = tk.Entry(self.contentFrame,
                                            width=25, show="*")
        self.senderPasswordEntry.grid(row=2, column=3, sticky=tk.W)

        self.recipientLabel = tk.Label(self.contentFrame, text="    Recipient")
        self.recipientLabel.grid(row=3, column=2, sticky=tk.W)
        self.recipientEntry = tk.Entry(self.contentFrame, width=25)
        self.recipientEntry.grid(row=3, column=3, sticky=tk.W)

        self.iterScaleLabel = tk.Label(self.contentFrame,
                                       text="    Times to send")
        self.iterScaleLabel.grid(row=4, column=2)
        self.iterScale = tk.Scale(self.contentFrame,
                                  from_=1,
                                  to=20,
                                  orient=tk.HORIZONTAL)
        self.iterScale.grid(row=4, column=3)

        self.contentLabel = tk.Label(self.contentFrame, text="Content")
        self.contentLabel.grid(row=5, column=2)
        self.content = tkst.ScrolledText(self.contentFrame,
                                         wrap=tk.WORD,
                                         width=25,
                                         height=10)
        self.content.grid(row=5, column=3, pady=(20))

        self.warningLabel = tk.Label(self.contentFrame,
                                     text="Please be patient!")
        self.warningLabel.grid(row=6, column=3)

        self.sendButton = tk.Button(self.contentFrame,
                                    text="Send",
                                    command=lambda:
                                    self.handleSendMailSMTP(
                                        self.senderEntry.get(),
                                        self.senderPasswordEntry.get(),
                                        self.recipientEntry.get(),
                                        self.content.get("1.0", "end"),
                                        self.iterScale.get())
                                    )
        self.sendButton.grid(row=6, column=2)

        self.contentFrame.grid(row=1, column=2)

    def handleSendMailSMTP(self, sender, pword, recip, cont, iters):
        """Call the function which actually sends the email."""
        if sendMail(sender, pword, recip, cont, iters):
            messagebox.showinfo("Success", "Your email has been sent")
        else:
            messagebox.showerror("Error", "Please check the values and retry")

    def clearContent(self):
        """Clear all content from the content frame."""
        for item in self.contentFrame.winfo_children():
            item.destroy()
