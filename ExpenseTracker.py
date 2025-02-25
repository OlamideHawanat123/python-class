class ExpenseTracker:
	def _init_(self):
		self.expense = []

	def add_expense(self):
		date = (input("Enter the date(YYYY-MM-DD: "))
		description = (str(input("Enter the description: ")))
		while True:
			try:
				amount = (float(input("Enter the amount: ")))
				break
			except ValueError:
				print('invalid amount, enter correct value')
				self.expense.append({
				"date": date,
				"description": description,
				"amount": amount
				}) 
				return self.display()
	def view_expenses(self):
		if not self.expense:
			print("Nothing is inside")
		else:
			print("Expense:")
			for count in self.expense:
				print(f'Date: {count['date']}, Description{count['description']}, Amount: ${count['amount']:.2f}')
		return self.display()
	def total_expenses(self):
		total = sum(count['amount'] for count in self.expense)
		print(f'total expense: ${total:.2f}')
		return self.display
	def exit_app(self):
		print("Exiting the app, thank you")
		exit()


	

	def display(self):
		print("""
		Welcome to Semicolon Expense Tracker App
		—----------------------------------------------------------------------------------
		1. Add an expense
		2. View all expenses
		3. Calculate total expenses
		4. Exit
		""")

		choice = int(input("Enter your preferred choice: "))

		match choice:
			case 1:
	    			return self.add_expense() 
			case 2:
				return self.view_expenses()
			case 3:
				return self.total_expenses()
			case 4: 
				return self.exit_app()
			case _:
				print("Invalid choice, please choose wisely")
				return self.display


def main():
	tracker = ExpenseTracker()
	tracker.display()

main()

	

		


		
		
		
		