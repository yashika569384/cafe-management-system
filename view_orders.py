import tkinter as tk
from tkinter import messagebox, ttk
import db
import admin_dash
from PIL import Image, ImageTk

# Tkinter application setup
class AdminDashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Admin Dashboard")
        self.root.geometry("2000x1000") # 800 600
        self.root.resizable(True, True)

        # Bill number input field
        self.bill_number = tk.StringVar()

        # Interface elements
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):

        self.image = Image.open("coffe.jpg")
        self.image = self.image.resize((2000,600))
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = tk.Label(self.root, image=self.photo)
        self.label.place(x=0, y=0)
        # Title
        
        self.image1 = Image.open("bak.png")
        self.image1 = self.image1.resize((60,40))
        self.photo1 = ImageTk.PhotoImage(self.image1)

        self.label1 = tk.Button(self.root, image=self.photo1, command=self.back)
        self.label1.place(x=0, y=0)
        
        tk.Label(self.root, text="Admin Dashboard", font=("Helvetica", 24, "bold")).pack(pady=10)

        # Bill number input
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=30)

        tk.Label(input_frame, text="Bill Number:", font=("time", 14)).grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(input_frame, textvariable=self.bill_number, font=("time", 14),width=10).grid(row=0, column=1, padx=10, pady=5)

        # Fetch orders button
        tk.Button(input_frame, text="View Orders", command=self.view,font=("time", 12)).grid(row=1, column=0, padx=10, pady=5)

        tk.Button(input_frame, text="View All Orders", command=self.viewall,font=("time", 12)).grid(row=1, column=1, padx=10, pady=5)

        # Table for displaying orders
        self.orders_table = ttk.Treeview(self.root, columns=("Bill Number", "date", "name", "item name", "Price", "bill detail"), show='headings')
        self.orders_table.heading("Bill Number", text="Bill Number")
        self.orders_table.heading("date", text="date")
        self.orders_table.heading("name", text="name")
        self.orders_table.heading("item name", text="item name")
        self.orders_table.heading("Price", text="Price")
        self.orders_table.heading("bill detail", text="bill detail")
        self.orders_table.column("Bill Number", width=50)
        self.orders_table.column("date", width=80)
        self.orders_table.column("name", width=80)
        self.orders_table.column("item name", width=80)
        self.orders_table.column("Price", width=50)
        self.orders_table.column("bill detail", width=100)  
        self.orders_table.pack(fill=tk.BOTH, expand=True)
    
    def back(self):
        self.root.destroy()
        admin_dash.AdminDashboard()
        

   # def view(self):
        # Clear the table
       # for item in self.orders_table.get_children():
       #     self.orders_table.delete(item)

        # Fetch orders based on bill number
        #orders = db.viewOrder(self.bill_number.get())

        #if orders:
           # for i in orders:
                #self.orders_table.insert("", "end", values=i)
        #else:
           # messagebox.showinfo("Info", "No orders found for this bill number.")



    def view(self):
    # Clear the table
        for item in self.orders_table.get_children():
            self.orders_table.delete(item)

        bill_number = self.bill_number.get().strip()  # Get input and remove extra spaces

        if not bill_number:  # Check if the input is empty
            messagebox.showerror("Error", "Please enter a bill number.")
            return

        if not bill_number.isdigit():  # Check if the input is not a valid number
            messagebox.showerror("Error", "Bill number must be a number.")
            return

    # Convert the bill number to an integer
        bill_number = int(bill_number)

    # Fetch the orders
        orders = db.viewOrder(bill_number)

        if orders:  # If orders are found, add them to the table
            for order in orders:
                self.orders_table.insert("", "end", values=order)
        else:
            messagebox.showinfo("Info", "No orders found for this bill number.")

    def viewall(self):
        # Clear the table
        for item in self.orders_table.get_children():
            self.orders_table.delete(item)

        # Fetch all orders
        orders = db.viewAllOrder()
        print(orders)

        if orders:
            for order in orders:
                self.orders_table.insert("", "end", values=order)
        else:
            messagebox.showinfo("Info", "No orders found.")

# Running the Tkinter application
if __name__ == "__main__":
    # root = tk.Tk()
    app = AdminDashboard()
    