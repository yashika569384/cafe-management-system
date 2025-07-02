import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from payment import PaymentScreen
import db

# Connect to MySQL database
def fetch_menu_items():
    items = db.viewMenu()
    print(items)
    return items

class CafeManagementSystem:
    def __init__(self, res):
        self.root = ctk.CTk()
        self.root.title("Cafe Management System")
        self.root.geometry("2000x1000")

        # Set the theme to dark
        ctk.set_appearance_mode("light")

        # Cart to hold selected items
        self.cart = []
        self.res = res
        print("---", self.res)
        
        # Create a main frame to hold both the menu items and the proceed button
        self.main_frame = ctk.CTkFrame(self.root)  # Change 'self' to 'self.root'
        self.main_frame.pack(fill="both", expand=True, side="left", padx=10, pady=10)

        # Create a scrollable frame to hold the menu items
        self.scrollable_menu_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color='#FBECB2', width=700, height=500)
        self.scrollable_menu_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Fetch menu items from the database
        self.menu_items = fetch_menu_items()

        # Display the menu items in the scrollable frame
        self.display_menu_items()

        # Create a right-side frame for cart items and proceed button
        self.cart_frame = ctk.CTkFrame(self.root, width=250, fg_color="white")  # Change 'self' to 'self.root'#gray30
        self.cart_frame.pack(side="right", fill="y", padx=10, pady=10)

        # Title label for the cart section
        cart_label = ctk.CTkLabel(self.cart_frame, text="Your Cart", font=("Arial", 18, "bold"), text_color="black")
        cart_label.pack(pady=10)

        # Proceed to Checkout button aligned to the bottom-right within the cart frame
        self.proceed_button = ctk.CTkButton(self.cart_frame, text="Proceed to Checkout", command=self.show_cart)
        self.proceed_button.pack(side="bottom", pady=10, padx=10)

        # Add a total price label that will be updated
        self.total_label = ctk.CTkLabel(self.cart_frame, text="Total: Rs.0.00", font=("Arial", 18, "bold"), text_color="black")
        self.total_label.pack(anchor="e", padx=10, pady=20)
        
        # Start the Tkinter main loop
        self.root.mainloop()

    # Function to display the menu items as cards in a scrollable frame
    def display_menu_items(self):
        row = 0
        column = 0
        for index, item in enumerate(self.menu_items):
            self.create_item_card(item, row, column)
            column += 1
            if column > 1:  # After placing two cards in a row, move to the next row
                column = 0
                row += 1

    # Function to create individual item cards in a scrollable grid
    def create_item_card(self, item, row, column):
        card = ctk.CTkFrame(self.scrollable_menu_frame, width=600, height=150, border_width=2, fg_color="white") #gray20#height=120 width-350
        
        card.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
        card.grid_propagate(False)
        
        # Load the image using PIL
        try:
            image_path = item[4]  # Assuming the image path is in the 5th column
            image = Image.open(image_path)
            image = image.resize((100, 80))  # Resize the image as needed
            ctk_image = ctk.CTkImage(light_image=image, size=(100, 80))  # Create a CTkImage
        except Exception as e:
            print(f"Error loading image: {e}")
            ctk_image = None

        # Display the image
        if ctk_image:
            image_label = ctk.CTkLabel(card, image=ctk_image, text="")
            image_label.grid(row=0, column=0, rowspan=3, padx=10, pady=5)

        # Item Name
        item_name = ctk.CTkLabel(card, text=item[1], font=("Arial", 14), text_color="black")#white
        item_name.grid(row=0, column=1, sticky="w", padx=10, pady=5)

        # Item Category
        item_category = ctk.CTkLabel(card, text=f"Category: {item[2]}", font=("Arial", 10), text_color="black")#lightgray
        item_category.grid(row=1, column=1, sticky="w", padx=10)

        # Item Price
        item_price = ctk.CTkLabel(card, text=f"Price: Rs.{item[3]:.2f}", font=("Arial", 10), text_color="black")#lightgray
        item_price.grid(row=2, column=1, sticky="w", padx=10)

        # Add to Cart Button
        add_to_cart_button = ctk.CTkButton(card, text="Add to Cart", fg_color="light blue", text_color="black", hover_color="gray40", command=lambda: self.add_to_cart(item))    #fg=gray30
        add_to_cart_button.grid(row=0, column=2, padx=10, pady=5)
                                                    #text=white
    # Function to handle adding items to the cart
    def add_to_cart(self, item):
        self.cart.append(item)
        self.update_cart_frame()  # Update cart when an item is added
        messagebox.showinfo("Success", f"{item[1]} added to cart!")

    # Function to update the cart frame and display items dynamically
    def update_cart_frame(self):
        # Clear existing widgets in cart frame except the total label and proceed button
        for widget in self.cart_frame.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and "Total" not in widget.cget("text") and widget != self.total_label:
                widget.destroy()

        # Display items in the cart
        for index, item in enumerate(self.cart):
            item_label = ctk.CTkLabel(self.cart_frame, text=f"{item[1]} - Rs.{item[3]:.2f}", font=("Arial", 14), text_color="black")
            item_label.pack(anchor="w", padx=10, pady=5)

        # Total Price Calculation
        self.total_price = sum([item[3] for item in self.cart])
        self.total_label.configure(text=f"Total: Rs.{self.total_price:.2f}")

    # Function to show a summary of the cart in a message box when proceeding to checkout
    def show_cart(self):
        if not self.cart:
            messagebox.showwarning("Cart Empty", "Your cart is empty!")
            return

        # Proceed to the payment screen
        self.proceed_to_payment()

    # Function to show the payment screen
    def proceed_to_payment(self):
        PaymentScreen(self, self.total_price, False, self.res)  # Open the payment screen with total price


# Run the application
if __name__ == "__main__":
    app = CafeManagementSystem((1, 'gurminder', 'gurminder@gmail.com'))
