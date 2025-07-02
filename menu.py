import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox, filedialog
import db
from PIL import Image, ImageTk
import shutil
import os
import tkinter as tk 
import admin_dash

class AdminDashboard:
    def __init__(self):
        self.root = ttk.Window(themename="flatly")
        self.root.title("Admin Dashboard - Cafe Management System")
        self.root.geometry("2000x1000") #1100 800
        self.root.resizable(True, True)

        # Menu item fields
        self.item_name = ttk.StringVar()
        self.category_id = ttk.StringVar()
        self.price = ttk.IntVar()
        self.image_path = ""  # Will store the path of the uploaded image
        self.description = ttk.StringVar()
      
        # Interface elements
        self.create_widgets()
        self.root.mainloop()
        
    
    def back(self):
        self.root.destroy()
        admin_dash.AdminDashboard()
        

    def create_widgets(self):
        # Set up background image
        self.image = Image.open("coffe.jpg")
        self.image = self.image.resize((1100, 600))
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = ttk.Label(self.root, image=self.photo)
        self.label.place(x=0, y=0)

        # Title with modern theme
        ttk.Label(self.root, text="Add Menu", font=("Helvetica", 24, "bold"), style="TLabel").pack(padx=(0, 0), pady=18)

        # Input fields with transparent background effect
        form_frame = ttk.Frame(self.root, style="TFrame")
        form_frame.pack(pady=20)
        
        self.image1 = Image.open("bak.png")
        self.image1 = self.image1.resize((60,40))
        self.photo1 = ImageTk.PhotoImage(self.image1)

        self.label1 = tk.Button(self.root, image=self.photo1, command=self.back)
        self.label1.place(x=0, y=0)

        ttk.Label(form_frame, text="Item Name", font=("time", 14), style="TLabel").grid(row=0, column=0, padx=10, pady=5)
        ttk.Entry(form_frame, textvariable=self.item_name, style="TEntry").grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(form_frame, text="Category", style="TLabel").grid(row=1, column=0, padx=10, pady=5)
        self.category_id_entry = ttk.Combobox(form_frame, textvariable=self.category_id, values=['Hot','Cold','Dessert','Snacks','Juice'])
        self.category_id_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(form_frame, text="Price", style="TLabel").grid(row=2, column=0, padx=10, pady=5)
        self.price_entry = ttk.Entry(form_frame, textvariable=self.price, style="TEntry")
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)

        # Upload Button instead of Image Entry
        ttk.Label(form_frame, text="Image", style="TLabel").grid(row=3, column=0, padx=10, pady=5)
        ttk.Button(form_frame, text="Upload Image", command=self.upload_file, style="TButton").grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(form_frame, text="Description", style="TLabel").grid(row=4, column=0, padx=10, pady=5)
        self.description_entry = ttk.Entry(form_frame, textvariable=self.description, style="TEntry")
        self.description_entry.grid(row=4, column=1, padx=10, pady=5)

        # Buttons for CRUD operations
        button_frame = ttk.Frame(self.root, style="TFrame")
        button_frame.pack(pady=20)

        ttk.Button(button_frame, text="Add Menu Item", command=self.add_item, style="TButton").grid(row=0, column=0, padx=10)
        ttk.Button(button_frame, text="View Menu", command=self.view_items, style="TButton").grid(row=0, column=1, padx=10)
        ttk.Button(button_frame, text="Update Selected", command=self.update_item, style="TButton").grid(row=0, column=2, padx=10)
        ttk.Button(button_frame, text="Delete Selected", command=self.delete_item, style="TButton").grid(row=0, column=3, padx=10)

        # Table for displaying menu items
        self.menu_table = ttk.Treeview(self.root, columns=("ID", "Name", "Category", "Price", "Image", "Description"), show='headings', style="TTreeview")
        self.menu_table.heading("ID", text="ID")
        self.menu_table.heading("Name", text="Name")
        self.menu_table.heading("Category", text="Category")
        self.menu_table.heading("Price", text="Price")
        self.menu_table.heading("Image", text="Image")
        self.menu_table.heading("Description", text="Description")
        self.menu_table.pack(fill=ttk.BOTH, expand=True)
        self.menu_table.column("ID", width=100)
        self.menu_table.column("Name", width=100)
        self.menu_table.column("Category", width=100)
        self.menu_table.column("Price", width=100)
        self.menu_table.column("Image", width=100)
        self.menu_table.column("Description", width=100)

        # Event binding for selecting an item in the table
        self.menu_table.bind("<ButtonRelease-1>", self.on_item_select)

    def upload_file(self):
        # Open a file dialog and select a file
        file_path = filedialog.askopenfilename()
        
        if file_path:
            try:
                # Define the target directory to save the file
                target_directory = "uploaded_files"
                
                # Create the target directory if it doesn't exist
                if not os.path.exists(target_directory):
                    os.makedirs(target_directory)
                
                # Extract the file name from the file path
                file_name = os.path.basename(file_path)
                
                # Define the target file path
                target_file_path = os.path.join(target_directory, file_name)
                
                # Copy the selected file to the target directory
                shutil.copy(file_path, target_file_path)
                
                # Store the file path in the image_path attribute
                self.image_path = target_file_path
                
                # Show a success message
                messagebox.showinfo("Success", f"File '{file_name}' uploaded successfully!")
            
            except Exception as e:
                # Show an error message if something goes wrong
                messagebox.showerror("Error", f"Failed to upload file: {str(e)}")
        else:
            messagebox.showwarning("No File", "No file was selected.")

    def add_item(self):
        # Get all values
        item_name = self.item_name.get()
        category_id = self.category_id.get()
        price = self.price.get()
        image_path = self.image_path
        description = self.description.get()

        # Prepare data for database insertion
        data = (item_name, category_id, price, image_path, description)

        # Insert data into the database
        res = db.addMenu(data)
        if res:
            messagebox.showinfo("Success", "Menu item added successfully!")
            self.clear_form()
            self.view_items()
        else:
            messagebox.showerror("Error", "Failed to add menu item.")

    def view_items(self):
        for item in self.menu_table.get_children():
            self.menu_table.delete(item)
        rows = db.viewMenu()
        for row in rows:
            self.menu_table.insert("", "end", values=row)

    def update_item(self):
        selected_item = self.menu_table.selection()
        if selected_item:
            item = self.menu_table.item(selected_item)["values"]
            data = (self.item_name.get(), self.category_id.get(), self.price.get(), self.image_path, self.description.get(), item[0])
            ress = db.updateMenu(data)
            if ress:
                messagebox.showinfo("Success", "Menu item updated successfully!")
                self.clear_form()
                self.view_items()
            else:
                messagebox.showerror("Error", "Failed to update menu item.")
        else:
            messagebox.showwarning("Warning", "Please select an item to update.")

    def delete_item(self):
        selected_item = self.menu_table.selection()
        if selected_item:
            item = self.menu_table.item(selected_item)["values"]
            ress = db.deleteMenu(item[0])
            if ress:
                messagebox.showinfo("Success", "Menu item deleted successfully!")
                self.view_items()
            else:
                messagebox.showerror("Error", "Failed to delete menu item.")
        else:
            messagebox.showwarning("Warning", "Please select an item to delete.")

    def on_item_select(self, event):
        selected_item = self.menu_table.selection()
        if selected_item:
            item = self.menu_table.item(selected_item)["values"]
            self.item_name.set(item[1])
            self.category_id.set(item[2])
            self.price.set(item[3])
            self.image_path = item[4]  
            self.description.set(item[5])

    def clear_form(self):
        self.item_name.set("")
        self.category_id.set(0)
        self.price.set(0.0)
        self.image_path = ""  
        self.description.set("")

if __name__ == "__main__":
    # root = ttk.Window(themename="flatly")
    app = AdminDashboard()
    # root.mainloop()
