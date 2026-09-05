import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

#Create CSV file if it does not exist

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            write = csv.writer(file)
            write.writerow(["Date", "Category","Description","Amount"])
# Adda new expense
def add_expense():

    date = input("Enter data (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Shopping/Bills/Other): ") 
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("Please enter a valid amount.")
        return
    try:
        datetime.strptime(date, "%d-%m-%Y") 
    except ValueError:
        print("Invalid date fromat. Use DD-MM-YYYY.")
        return
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            date,
            category,
            description,
            amount
        ])         
    print("Expense added successfully!")

#View all Expenses
def view_expenses():

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        #next(reader)

        print("\n========== ALL EXPENSES ==========")


        print(
               f"{'Date':<12} "
               f"{'Category':<12} "
               f"{'Description':<20} "
               f"{'Amount':<12} "

            )
        print("-" * 58)

        found = False
        
        for row in reader:
            found = True

            print(
                 f"{row['Date']:<12} "
                f"{row['Category']:<12} "
                f"{row['Description']:<20} "
                f"{float(row['Amount']):>10.2f} "
            
             )

       

        if not found:
            print("No expenses available.")


#Display spending summary
def spending_summary():

    total = 0
    category_totals = {}

    with open(FILE_NAME, "r")as file:
        reader = csv.DictReader(file)

        for row in reader:

            amount = float(row["Amount"])
            category = row["Category"]

            total += amount

            category_totals[category] = (
                category_totals.get(category,0) + amount
            )

    print("\n==================== SPENDING SUMMARY ===============")


    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")
    print(f"\nTotal Spending: ₹{total:.2f}")  
#Display monthly report
def monthly_report():

    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    total = 0
    category_totals = {}

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            date = datetime.strptime(row["Date"], "%d-%m-%Y")

            if (
                date.month == int(month)
                and date.year == int(year)
            ):

                amount = float(row["Amount"])
                category = row["Category"]

                total += amount

                category_totals[category] = (
                    category_totals.get(category, 0) + amount
                )
    print("\n=============== MONTHLY REPORT ===============")
    print(f"Month: {month}/{year}")  

    if not category_totals:
        print("NO expenses found for this month.")
        return        

    for category, amount in category_totals.items():
        print(f"{category}: ₹{total:.2f}")
#Create CSV file
create_file() 

#Main menu
while True:
    print("\n===========================================================")
    print("               EXPENSE TRACKER SYSTEM")
    print("\n===========================================================")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Spending Summary")
    print("4. Monthly Report")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        spending_summary()

    elif choice == "4":
        monthly_report()

    elif choice == "5":
        print("\nThank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")

  
