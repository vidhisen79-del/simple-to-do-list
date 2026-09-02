# Simple Expense Tracker Program

total = 0

while True:
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Total Spent")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        try:
            expense = int(input("Enter expense amount: "))

            if expense < 0:
                print("Expense cannot be negative.")
            else:
                total += expense
                print("Expense added successfully!")

        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "2":
        print(f"\nTotal Spent: ₹{total}")

    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")