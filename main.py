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
def add_asset(asset_id, asset_name, category, location, status):
    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([asset_id, asset_name, category, location, status])

# Display all IT assets
def display_assets():
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print("No assets found. Please initialize the file.")

# Example usage
initialize_file()
add_asset("101", "Dell Laptop", "Laptop", "Office A", "Available")
add_asset("102", "Cisco Router", "Network Device", "Server Room", "In Use")
display_assets()
