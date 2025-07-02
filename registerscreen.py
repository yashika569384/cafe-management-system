from tkinter import *
from PIL import Image, ImageTk
import re
from tkinter import messagebox
#import database
import db
import userlogin1
import admin_login
import menu
class homepage():
    def __init__ (self):
        self.root=Tk()
        self.root.title("user register")
        self.root.geometry("1000x700")
        self.frame1=Frame(self.root,background="",width=648,height=400)
        self.frame1.place(x=30,y=30)
        disp_width= self.root.winfo_screenwidth()
        disp_height= self.root.winfo_screenheight()
        self.root.geometry(f'{disp_width}x{disp_height}')
       
        img= Image.open('CAFElog15.jpg')
        img_new= img.resize((disp_width,disp_height))
        img_new=img.resize((1200,900))
        img_tk= ImageTk.PhotoImage(img_new)
 
        img_label= Label(self.root,image=img_tk)
        img_label.place(x=500,y=0) #AF8F6F
        self.frame6=Frame(self.root,background="white" ,width=80,height=60)
        self.frame6.place(x=520,y=0)
        self.frame1=Frame(self.root,background="#FBECB2",width=600,height=1000)
        self.frame1.place(x=0,y=0)
        
        #self.frame3=Frame(self.root,background='#F8BDEB',width=40,height=740)
        #self.frame3.place(x=520,y=30)
       # self.frame4=Frame(self.root,background='#F8BDEB',width=520,height=40)
        #self.frame4.place(x=0,y=730)
        #self.frame3=Frame(self.root,background='white',width=40,height=740)
        #self.frame3.place(x=560,y=60)
       # self.frame5=Frame(self.root,background='white',width=560,height=740)
       # self.frame5.place(x=0,y=760)


        self.label1=Label(self.frame1,text="-------SIPSTERS-------",background='#FBECB2',font=("Copperplate Gothic Light", 40 ,"bold") ,foreground="black")
        self.label1.place(x=50,y=40)
        self.label2=Label(self.frame1,text="Register",background='#FBECB2',font=("Copperplate Gothic Light", 20 ,"bold") ,foreground="black")
        self.label2.place(x=180,y=110)
        self.label3=Label(self.frame1,text="-----------Enter your details-----------",background='#FBECB2',font=("Copperplate Gothic Light", 15 ,"bold") ,foreground="black")
        self.label3.place(x=120,y=170)
        self.name=Label(self.frame1, text="Enter Name----------", background='#FBECB2' ,foreground='black' , font=("Cascadia code", 20))
        self.name.place(x=30,y=200)
        self.name_entry=Entry(self.frame1, text="Name", foreground="black" , font=("Arial", 19))
        self.name_entry.place(x=100,y=250)

        self.mail=Label(self.frame1, text="Enter your Email----", background='#FBECB2' ,foreground='black' , font=("Cascadia code", 20))
        self.mail.place(x=30,y=300)
        self.mail_entry=Entry(self.frame1, text="mail", foreground="black" , font=("Arial", 19))
        self.mail_entry.place(x=100,y=350)

        
        self.passw=Label(self.frame1, text="Create password-----", background='#FBECB2' ,foreground='black' , font=("Cascadia code", 20))
        self.passw.place(x=30,y=400)
        self.passw_entry=Entry(self.frame1,foreground="black" , font=("Arial", 19), show="*")
        self.passw_entry.place(x=100,y=450)
        self.num=Label(self.frame1,  text="Enter your Phone no.-", background="#FBECB2", foreground='black', font=("Cascadia code", 20) )
        self.num.place(x=30,y=500)
        self.num_entry=Entry(self.frame1 ,foreground="black" , font=("Arial", 19))
        self.num_entry.place(x=100,y=550)

        self.btn=Button(self.frame1, text="Register",  background="#05d7ff"    , foreground="Black"  , activebackground="#65e7ff"    , activeforeground="Black" , highlightthickness=2, highlightbackground="#05d7ff"
                      ,  highlightcolor="White", width=10, height=1,font=('Arial',13, "bold") ,command=self.registerUser)
        self.btn.place(x=180,y=600)
        self.label5=Label(self.frame1, text="Or ", background='#FBECB2' ,foreground='black' , font=("Copperplate Gothic Light", 10,"bold "))
        self.label5.place(x=195,y=650)
        self.label4=Label(self.frame1, text="Already Registered", background='#FBECB2' ,foreground='black' , font=("Copperplate Gothic Light", 15,"bold "))
        self.label4.place(x=50,y=670)
        self.btn2=Button(self.frame1, text="Sign in as user",  background="#05d7ff"    , foreground="Black"  , activebackground="#65e7ff"    , activeforeground="Black" , highlightthickness=2, highlightbackground="#05d7ff"
                      ,  highlightcolor="White", width=12, height=1,font=('Arial',13, "bold") ,command=self.getsign )
        self.btn2.place(x=300,y=650)

        self.btn1=Button(self.frame1, text="Sign in as admin",  background="#05d7ff"    , foreground="Black"  , activebackground="#65e7ff"    , activeforeground="Black" , highlightthickness=2, highlightbackground="#05d7ff"
                      ,  highlightcolor="White", width=12, height=1,font=('Arial',13, "bold"), command=self.getadmin)
        self.btn1.place(x=300,y=700)
        
        

        self.root.mainloop()

    def registerUser(self):
        
        
        self.data=(self.name_entry.get(), self.mail_entry.get(), self.passw_entry.get(), self.num_entry.get())
        print(self.data)
        



        if (self.mail_entry.get()=="") or (self.name_entry.get()=="") or  (self.passw_entry.get()=="") or (self.num_entry.get()=="") :
              
              messagebox.showwarning("showwarning", "Warning fill your requird field") 

        
        

        



        patt="[a-zA-z0-9_]"
        number=self.num_entry.get()
        patternum="^[6-9]{1}\d{9}"
        pasword=self.passw_entry.get()
        emailid=self.mail_entry.get()
        pattern="[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]{2,6}"
        check1=re.match(pattern,emailid)
        check2=re.match(patt,pasword)
        check3= re.match(patternum,number)
        if check1 is None:
             print("invalid email id")
             messagebox.showerror("showwarning", "Warning fill valid email id")
        elif check2 is None:
             print("invalid password")
             messagebox.showerror("showwarning", "Warning fill valid password")
        elif check3 is None:
            print("Invalid Number")
            messagebox.showerror("showwarning", "Warning fill valid number")
        else:
            res=db.registerUser(self.data)
            if res:
                messagebox.showinfo("Database","User Registered Successfully")
                self.root.destroy()
                userlogin1.loginPage()
            else:
                messagebox.showerror("Error","Not Registered Successfully")

    def next(self):
        
        self.root.destroy()
        userlogin1.loginPage()

    # def combined(self):
    #     registerUser(self)
    #     next(self)
            

        


            


        


    def getsign(self):
       self.root.destroy()
       userlogin1.loginPage()



    def getadmin(self):
        self.root.destroy()
        admin_login.loginPage()





       #self.btn=Button(self.frame1, text="Sign up",  background="#05d7ff"    , foreground="Black"  , activebackground="#65e7ff"    , activeforeground="Black" , highlightthickness=2, highlightbackground="#05d7ff"
                     # ,  highlightcolor="White", width=10, height=1,font=('Arial',13, "bold"))
       # self.btn.place(x=180,y=650)

    


    

    


        
        

        
        
       
        
   
       

if __name__=="__main__":

  homepage()



    