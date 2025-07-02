from tkinter import *
from PIL import Image, ImageTk  # Requires Pillow library
import menu
import db
import view_orders

class AdminDashboard:
    def __init__(self):
        self.root = Tk()
        self.root.title("Admin Dashboard")
        self.root.geometry("2000x1000")
        self.root.resizable(True, True)

        self.im=Image.open("coffe.jpg")
        self.im=self.im.resize((2000,1000))#800,500
        self.photo=ImageTk.PhotoImage(self.im)
        self.label=Label(self.root,image=self.photo)
        self.label.place(x=0,y=0)

        # Load and resize images
        self.orders_img = Image.open("image.png")  
        self.orders_img = self.orders_img.resize((200, 200))#100,100
        self.orders_photo = ImageTk.PhotoImage(self.orders_img)

        self.menu_img = Image.open("image.png")  
        self.menu_img = self.menu_img.resize((200, 200))#100,100
        self.menu_photo = ImageTk.PhotoImage(self.menu_img)

        self.users_img = Image.open("image.png")  
        self.users_img = self.users_img.resize((100, 100))#100,100
        self.users_photo = ImageTk.PhotoImage(self.users_img)

        self.del_img = Image.open("image.png")  
        self.del_img = self.del_img.resize((100, 100))#100,100
        self.del_photo = ImageTk.PhotoImage(self.del_img)

        # Use grid layout to position buttons and labels evenly



        self.btn_view_orders = Button(self.root, image=self.orders_photo, command=self.view_orders_page)
        self.btn_view_orders.place(x=1200,y=30)

        self.l1 = Label(self.root, text="View Orders", font=("Helvetica", 12))
        self.l1.place(x=1200,y=250)

        self.btn_view_menu = Button(self.root, image=self.menu_photo, command=self.view_menu_page)
        self.btn_view_menu.place(x=1200,y=350)

        self.l2 = Label(self.root, text="View Menu", font=("Helvetica", 12))
        self.l2.place(x=1200,y=570)
        

    

        self.root.mainloop()

    def view_orders_page(self):
        self.root.destroy()
        view_orders.AdminDashboard()

    def view_menu_page(self):
        self.root.destroy()
        menu.AdminDashboard()




if __name__ == "__main__":
    AdminDashboard()