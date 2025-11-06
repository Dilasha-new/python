from datetime import datetime

# Ask the user to enter a date
date_input = input("Enter a date (YYYY-MM-DD): ")

try:
    # Convert the input string to a datetime object
    date_object = datetime.strptime(date_input, "%Y-%m-%d")
    print("You entered the date:", date_object.date())
except ValueError:
    print("Invalid date format. Please enter in YYYY-MM-DD format.")

if 