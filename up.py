from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image,ImageTk
import shutil
import os
import db
def upload_file():
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
            print(target_file_path)
            # print("Target directory ",target_directory)
            print("Target file path ",target_file_path)   # save this path in database
            # Copy the selected file to the target directory
            shutil.copy(file_path, target_file_path)
            
            
            # Show a success message
            messagebox.showinfo("Success", f"File '{file_name}' uploaded successfully!")
        
        except Exception as e:
            # Show an error message if something goes wrong
            messagebox.showerror("Error", f"Failed to upload file: {str(e)}")
    else:
        messagebox.showwarning("No File", "No file was selected.")
        
        
upload_file()