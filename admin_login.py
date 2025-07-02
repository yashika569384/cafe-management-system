from customtkinter import *
from PIL import Image

from tkinter import messagebox
import admin_dash
import db

class loginPage:
    def __init__(self):
        self.main = CTk()
        self.main.title("Login Page")
        self.main.config(bg="white")
        self.main.geometry("2000x1000")
        self.main.resizable(True, True)
        #background image  D9D9D9  #0085FF
        self.bg_img = CTkImage(dark_image=Image.open("bg1.jpg"), size=(900, 900))
        self.bg_lab = CTkLabel(self.main, image=self.bg_img, text="")
        self.bg_lab.place(x=0, y=0)



        #self.bg_img = CTkImage(dark_image=Image.open("bg1.jpg"), size=(500, 500))

      #  self.bg_lab = CTkLabel(self.main, image=self.bg_img, text="")
      #  self.bg_lab.grid(row=0, column=0)
        #self.frame1 = CTkFrame(self.main, fg_color="#D9D9D9", bg_color="white",  width=670,height=760, corner_radius=20)
       
        #self.frame1.place(x=830, y=20)  
         # Login Frame
        self.frame1 = CTkFrame(self.main, fg_color="#D9D9D9", width=700,height=800, corner_radius=20 )
       
        self.frame1.place(x=830, y=0)  

        # Title
        self.title = CTkLabel(self.frame1, text="Welcome Back Admin!\nLogin to Account", 
                              text_color="black", font=("Arial", 52, "bold"))
        self.title.place(x=100, y=50)

        # Username Entry

        self.usrname1=CTkLabel(self.frame1, text_color="black",text="Username",font=("Arial",15,"bold"))
        self.usrname1.place(x=150,y=210)
        self.usrname_entry = CTkEntry(self.frame1, text_color="white", placeholder_text="Username", 
                                      fg_color="black", placeholder_text_color="white", 
                                      font=("Arial", 16), width=390, corner_radius=15, height=50)
        self.usrname_entry.place(x=150, y=250)

        # Password Entry
        self.password=CTkLabel(self.frame1, text_color="black",text="password",font=("Arial",15,"bold"))
        self.password.place(x=150,y=310)

        self.passwd_entry = CTkEntry(self.frame1, text_color="white", placeholder_text="Password", 
                                     fg_color="black", placeholder_text_color="white", 
                                     font=("Arial", 16), width=390, corner_radius=15, height=50, show="*")
        self.passwd_entry.place(x=150, y=350)  


        #self.frame1 = CTkFrame(self.main,fg_color="#D9D9D9", bg_color="white", height=350, width=300,corner_radius=20)
       # self.frame1.grid(row=0, column=1,padx=40)

        #self.title = CTkLabel(self.frame1, text="Welcome Back Admin!\nLogin to Account", 
                              #text_color="black", font=("Arial", 52, "bold"))
        #self.title.place(x=100, y=50)




        #self.title = CTkLabel(self.frame1,text="Welcome Back! \nLogin to Account",text_color="black",font=("",35,"bold"))
        #self.title.grid(row=0,column=0,sticky="nw",pady=30,padx=10)

        #self.usrname_entry = CTkEntry(self.frame1,text_color="white", placeholder_text="Username", fg_color="black", placeholder_text_color="white",
                               ## font=("",16,"bold"), width=200, corner_radius=15, height=45)
       # self.usrname_entry.grid(row=1,column=0,sticky="nwe",padx=30)

        #self.passwd_entry = CTkEntry(self.frame1,text_color="white",placeholder_text="Password",fg_color="black",placeholder_text_color="white",
                                #font=("",16,"bold"), width=200,corner_radius=15, height=45, show="*")
        #self.passwd_entry.grid(row=2,column=0,sticky="nwe",padx=30,pady=20)


        self.l_btn = CTkButton(self.frame1, text="Login", font=("Arial", 15, "bold"), 
                               height=45, width=150, fg_color="#6F4E37", cursor="hand2", 
                               corner_radius=15, command=self.login)
        self.l_btn.place(x=250, y=500)
        self.main.mainloop()
        
    def login(self):
        data= (self.usrname_entry.get(),self.passwd_entry.get())
        res= db.loginAdmin(data)
        if res:
            messagebox.showinfo("Success",'Admin Login Successfully')
            self.main.destroy()
            admin_dash.AdminDashboard()
            
        else:
            messagebox.showerror("Error",'Not Exist')
            
            
        
if __name__=='__main__':
    obj=loginPage()
    