expenses = [] 

def add_expense():
	date = input("Enter the date(YYYY-MM-DD): ")
	description = input("Enter the description: ")
	while True:
		try:
			amount = float(input("Enter amount: "))
			expenses.append({
			'date': date,
			'description': description,
			'amount': amount
			})
		except ValueError:
			print('Invalid amount, enter a valid input')
		return display()
def view_expenses():
		if not expenses:
			print("Empty expense list, go add")
		else:
			print("Expense:")
			for count in expenses:
				print(f'Date: {count["date"]}, Description: {count["description"]}, Amount: ${count["amount"]:.2f}')
		return display()

def calculate_total():
	total = sum(count['amount'] for count in expenses)
	print(f'total expense: ${total:.2f}')
	return display()

def exit():
	print('Exiting the app, thank you!!!')
	
	








def display():
	print("""
Welcome to Semicolon Expense Tracker App
--------------------------------------------------
1. Add an expense
2. View all expenses
3. Calculate total expenses
4. Exit
  	""") 
	
	try:
		choice = int(input("Enter your choice: "))
	except ValueError:
		print("Wetin you dey try do gangan")
		display()			
	match choice:
		case 1:
			return add_expense()
		case 2:
			return view_expenses()
		case 3:
			return calculate_total()
		case 4:
			return exit()
		case _:
			print('Invalid choice, choose wisely')
			display()
display()

