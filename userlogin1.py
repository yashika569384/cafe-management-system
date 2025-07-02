from customtkinter import *
from PIL import Image
from tkinter import messagebox
import view_menu
import db

class loginPage:
    def __init__(self):
        self.main = CTk()
        self.main.title("Login Page")
        self.main.config(bg="white")
        self.main.geometry("2000x1000")

        # Background Image
        self.bg_img = CTkImage(dark_image=Image.open("image.png"), size=(800, 800))
        self.bg_lab = CTkLabel(self.main, image=self.bg_img, text="")
        self.bg_lab.place(x=0, y=0)
        #self.frame2=CTkFrame(self.main, fg_color="#EADDCA", width=1000,height=800)
       # self.frame2.place(x=1000,y=20)#EADDCA

        # Login Frame
        self.frame1 = CTkFrame(self.main, fg_color="#FBECB2", width=800,height=800)
       
        self.frame1.place(x=800, y=0)  

        # Title
        self.title = CTkLabel(self.frame1, text="Welcome Back!\nLogin to Account", 
                              text_color="black", font=("Arial", 55, "bold"))
        self.title.place(x=100, y=50)

        # Username Entry

        self.usrname1=CTkLabel(self.frame1, text_color="black",text="Username",font=("Arial",19,"bold"))
        self.usrname1.place(x=123,y=220)
        self.usrname_entry = CTkEntry(self.frame1, text_color="white", placeholder_text="Username", 
                                      fg_color="black", placeholder_text_color="white", 
                                      font=("Arial", 16), width=360, corner_radius=15, height=50)
        self.usrname_entry.place(x=120, y=260)

        # Password Entry
        self.password=CTkLabel(self.frame1, text_color="black",text="password",font=("Arial",19,"bold"))
        self.password.place(x=123,y=340)

        self.passwd_entry = CTkEntry(self.frame1, text_color="white", placeholder_text="Password", 
                                     fg_color="black", placeholder_text_color="white", 
                                     font=("Arial", 16), width=360, corner_radius=15, height=50, show="*")
        self.passwd_entry.place(x=120, y=380)

        # Login Button
        self.l_btn = CTkButton(self.frame1, text="Login", font=("Arial", 15, "bold"), 
                               height=45, width=150, fg_color="#6F4E37", cursor="hand2", 
                               corner_radius=15, command=self.login)
        self.l_btn.place(x=225, y=500)

        self.main.mainloop()
        
    def login(self):
        data = (self.usrname_entry.get(), self.passwd_entry.get())
        res = db.loginUser(data)
        if res:
            messagebox.showinfo("Success", 'User Login Successfully')
            self.main.destroy()
            view_menu.CafeManagementSystem(res)
        else:
            messagebox.showerror("Error", 'Not Exist')


if __name__ == '__main__':
    obj = loginPage()
