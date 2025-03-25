import tkinter as tk
from tkinter import messagebox
import csv

# File to store IT assets
csv_file = "it_assets.csv"

# Initialize the CSV file with headers if it doesn't exist
def initialize_file():
    try:
        with open(csv_file, 'x', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Asset ID", "Asset Name", "Category", "Location", "Status"])
    except FileExistsError:
        pass

# Add a new IT asset
def add_asset():
    asset_id = entry_id.get()
    asset_name = entry_name.get()
    category = entry_category.get()
    location = entry_location.get()
    status = entry_status.get()

    if asset_id and asset_name and category and location and status:
        with open(csv_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([asset_id, asset_name, category, location, status])
        messagebox.showinfo("Success", "Asset added successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Please fill in all fields!")

# Display all IT assets
def display_assets():
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            assets = "\n".join([", ".join(row) for row in reader])
            messagebox.showinfo("Assets", assets)
    except FileNotFoundError:
        messagebox.showerror("Error", "No assets found. Please initialize the file.")

# Clear input fields
def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_location.delete(0, tk.END)
    entry_status.delete(0, tk.END)

# Initialize the file
initialize_file()

# Create the GUI
root = tk.Tk()
root.title("IT Asset Management System")

tk.Label(root, text="Asset ID").grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

tk.Label(root, text="Asset Name").grid(row=1, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

tk.Label(root, text="Category").grid(row=2, column=0)
entry_category = tk.Entry(root)
entry_category.grid(row=2, column=1)

tk.Label(root, text="Location").grid(row=3, column=0)
entry_location = tk.Entry(root)
entry_location.grid(row=3, column=1)

tk.Label(root, text="Status").grid(row=4, column=0)
entry_status = tk.Entry(root)
entry_status.grid(row=4, column=1)

tk.Button(root, text="Add Asset", command=add_asset).grid(row=5, column=0)
tk.Button(root, text="Display Assets", command=display_assets).grid(row=5, column=1)

root.mainloop()
