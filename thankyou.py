from tkinter import *
from PIL import Image , ImageTk
import customtkinter

class thankyoupage():
    def __init__(self):
        self.root=Tk() 
        self.root.title("Thankyou")
        self.root.geometry("2000x1000")
        self.root.resizable(True,True)
        
         #AF8F6F
        self.frame1=Frame(self.root,background="#002244" ,width=2100,height=1000)
        self.frame1.place(x=0,y=0)
        self.label1=Label(self.frame1,text="WE  WANT  TO  SAY",background='#002244',font= ("Bahnschrift SemiBold",23,"bold") ,foreground="#FF92A5") ##FFC0CB
        self.label1.place(x=630,y=100)
        self.label1=Label(self.frame1,text="THANK YOU",background='#002244',font=("Bahnschrift SemiBold Semiconden", 85,"bold") ,foreground="#90EE90")
        self.label1.place(x=530,y=150)
        self.label2=Label(self.frame1,text="FOR  BEING  A  GREAT",background='#002244',font=("Bahnschrift SemiBold", 23,"bold") ,foreground="#FF92A5")
        self.label2.place(x=620,y=300)
        self.label3=Label(self.frame1,text="CUSTOMER!",background='#002244',font=("Bahnschrift SemiBold", 23,"bold") ,foreground="#FF92A5")
        self.label3.place(x=673,y=350)
        self.label4=Label(self.frame1,text=". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  ",background='#002244',font=("Bahnschrift SemiBold", 23,"bold") ,foreground="#FF92A5")
        self.label4.place(x=530,y=400)
        self.label5=Label(self.frame1,text="THANKYOU  FOR  YOUR  CONTINUOUS  SUPPORT  AND  LOYALTY",background='#002244',font=("Bahnschrift SemiBold", 23,"bold") ,foreground="#FF92A5")
        self.label5.place(x=370,y=450)
        self.label6=Label(self.frame1,text="FOR CHOSSING OUR SERVICE",background='#002244',font=("Bahnschrift SemiBold", 23,"bold") ,foreground="#FF92A5")
        self.label6.place(x=600,y=500)
        self.label7=Label(self.frame1,text="WE  APPRECIATE  THE  OPPURTUNITY  TO  SERVE  YOU",background='#002244',font=("Bahnschrift SemiBold", 25,"bold") ,foreground="#FF92A5")
        self.label7.place(x=370,y=550)
        #self.label8=Label(self.frame1,text=". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  ",background='#002244',font=("Bahnschrift SemiBold", 23,"bold") ,foreground="#FF92A5")
        #self.label8.place(x=530,y=570)
        self.label8=Label(self.frame1,text="                    For further info you can contact us at  EMAIL-Sipsters@gmail.com",background='#002244',font=("Bahnschrift SemiBold", 15,"bold") ,foreground="#FF92A5")
        self.label8.place(x=370,y=610)
        self.label9=Label(self.frame1,text="                                                  CONTACT NO.-9876543211",background='#002244',font=("Bahnschrift SemiBold", 15,"bold") ,foreground="#FF92A5")
        self.label9.place(x=370,y=660)


        

        self.root.mainloop()

if __name__=="__main__":
    obj=thankyoupage()