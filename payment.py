import datetime
from decimal import Decimal
import customtkinter as ctk
from tkinter import messagebox
import db  # Assuming you have a database module for MySQL interaction
import thankyou
class PaymentScreen:
    def __init__(self, parent, total_price, is_first_time, res):
        # super().__init__(parent)
        self.root= ctk.CTkToplevel()
        self.root.title("Payment")
        self.root.geometry("400x650")
        self.root.focus()
        self.root.grab_set()

        self.res= res
        self.total_price = Decimal(total_price)  # Convert to Decimal for precision
        self.is_first_time = is_first_time  # Track if the user is a first-time visitor
        self.final_price = self.total_price  # Initialize final price to total price

        # Birthday Entry
        birthday_label = ctk.CTkLabel(self.root, text="Is it your birthday? (DD-MM format)", font=("Arial", 14))
        birthday_label.pack(pady=10)

        self.birthday_entry = ctk.CTkEntry(self.root, placeholder_text="Enter DD-MM")
        self.birthday_entry.pack(pady=10)

        # Total price label (Initial)
        self.total_label = ctk.CTkLabel(self.root, text=f"Total Amount: Rs.{self.total_price:.2f}", font=("Arial", 18, "bold"))
        self.total_label.pack(pady=20)

        # Payment Method dropdown
        method_label = ctk.CTkLabel(self.root, text="Select Payment Method", font=("Arial", 14))
        method_label.pack(pady=10)

        self.payment_method = ctk.StringVar(value="Select")
        payment_dropdown = ctk.CTkOptionMenu(self.root, variable=self.payment_method, values=["UPI", "Credit/Debit Card", "Net Banking", "Cash"])
        payment_dropdown.pack(pady=10)

        # Mobile Number entry
        mobile_label = ctk.CTkLabel(self.root, text="Mobile Number", font=("Arial", 14))
        mobile_label.pack(pady=10)

        self.mobile_entry = ctk.CTkEntry(self.root, placeholder_text="Enter Mobile Number")
        self.mobile_entry.pack(pady=10)

        # Email ID entry
        email_label = ctk.CTkLabel(self.root, text="Email ID", font=("Arial", 14))
        email_label.pack(pady=10)

        self.email_entry = ctk.CTkEntry(self.root, placeholder_text="Enter Email ID") #state='disable'
        self.email_entry.insert(0, self.res[2]) 
        self.email_entry.pack(pady=10)

        # Check Bill button to calculate and display final price with discount
        check_bill_button = ctk.CTkButton(self.root, text="Check Bill", command=self.check_bill)
        check_bill_button.pack(pady=10)

        # Submit button to submit the bill to the database (Initially disabled)
        self.submit_bill_button = ctk.CTkButton(self.root, text="Submit Bill", command=self.submit_bill_to_database, state="disabled")
        self.submit_bill_button.pack(pady=10)

    # Function to calculate discounted price based on birthday and first-time visit
    def calculate_discounted_price(self):
        discount = Decimal('0')  # Initialize discount as Decimal
        now = datetime.datetime.now()
        birthday_str = self.birthday_entry.get()

        try:
            # Check if it's the user's birthday
            birthday = datetime.datetime.strptime(birthday_str, "%d-%m")
            if birthday.day == now.day and birthday.month == now.month:
                discount = Decimal('0.60')  # 60% discount for birthdays
            elif self.is_first_time:
                discount = Decimal('0.40')  # 40% discount for first-time visitors
        except ValueError:
            messagebox.showerror("Error", "Invalid birthday format!")

        final_price = self.total_price * (Decimal('1') - discount)
        return final_price

    # Function to check the bill and display the final amount
    def check_bill(self):
        # Calculate the final price with discounts
        self.final_price = self.calculate_discounted_price()

        # Update the total label to show the final price after discount
        self.total_label.configure(text=f"Total Amount: Rs.{self.final_price:.2f}")

        # Enable the Submit Bill button
        self.submit_bill_button.configure(state="normal")

    # Function to submit the bill to MySQL database
    def submit_bill_to_database(self):
        method = self.payment_method.get()
        mobile = self.mobile_entry.get()
        email = self.email_entry.get()

        if method == "Select" or not mobile or not email:
            messagebox.showerror("Error", "Please fill in all fields before submitting the bill!")
            return

        now = datetime.datetime.now()
        d = now.strftime("%Y-%m-%d %H:%M:%S")

        # Assuming `database.add_payment` is a function that inserts the payment details into MySQL
        try:
            res = db.add_payment((self.final_price, method, mobile, email, d))
            if res:
                messagebox.showinfo("Success", "Bill submitted successfully!")
                self.root.destroy()
                thankyou.thankyoupage()
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to submit bill: {str(e)}")
