class ExpenseTracker:
    def __init__(self):
        self.expense = []

    def add_expense(self):
        date = input("Enter the date(YYYY-MM-DD): ")
        description = input("Enter the description: ")
        while True:
            try:
                amount = float(input("Enter the amount: "))
                self.expense.append({
                    "date": date,
                    "description": description,
                    "amount": amount
                })
                break  # Exit the loop if input is valid
            except ValueError:
                print('Invalid amount, enter a correct value')
        return self.display()

    def view_expenses(self):
        if not self.expense:
            print("Nothing is inside")
        else:
            print("Expenses:")
            for count in self.expense:
                print(f"Date: {count['date']}, Description: {count['description']}, Amount: ${count['amount']:.2f}")
        return self.display()

    def total_expenses(self):
        total = sum(count['amount'] for count in self.expense)
        print(f'Total expense: ${total:.2f}')
        return self.display()

    def exit_app(self):
        print("Exiting the app, thank you")
        exit()

    def display(self):
        print("""
        Welcome to Semicolon Expense Tracker App
        --------------------------------------------------
        1. Add an expense
        2. View all expenses
        3. Calculate total expenses
        4. Exit
        """)

        while True:  # Loop for valid input
            try:
                choice = int(input("Enter your preferred choice: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        if choice == 1:
            return self.add_expense()
        elif choice == 2:
            return self.view_expenses()
        elif choice == 3:
            return self.total_expenses()
        elif choice == 4:
            return self.exit_app()
        else:
            print("Invalid choice, please choose wisely")
            return self.display()

def main():
    tracker = ExpenseTracker()
    tracker.display()

if __name__ == "__main__":
    main()