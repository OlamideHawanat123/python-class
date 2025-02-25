tasks = []

def add_a_task():
	add_tasks = input("Enter the task: ")
	print("Task added !")
	tasks.append({
	'tasks': add_tasks})
	display()

def view_tasks():
	if not tasks:
		print("You haven't added any task")
	else:
		print("Tasks")
	for count in tasks:
		print(f' []{count["tasks"]}')
		print("======================================")
	display()

def mark_as_complete():
	if not tasks:
		print("You haven't added any task")
	else:
		for count in tasks:
			print(f' []{count["tasks"]}')
	mark_task = int(input("Which task have you completed: "))
	for count in tasks:
		print(f'[x] {count["tasks"]}')
	display()

		
	
def delete_task():
	if not tasks:
		print("You haven't added any task")
	else:
		delete_tasks = ("Which task do you wanyt to delete: ")
		global remove_element
		remove_element = tasks[delete_tasks]
		print("Removed successfully")
	display()
		
def exit():
	print("Exiting app, thank you")
		
		
		
	
	









	



def display():
	print("""
To-Do List Manager
1) Add a task
2) View tasks
3) Mark task as complete
4) Delete a task
5) Exit
""")

	try:
		choice = int(input("Enter your choice:"))
	except ValueError: 
		print("Enter a valid number, you fool!")
		display()

	match choice:
		case 1:
			return add_a_task()
		case 2:
			return view_tasks()
		case 3:
			return mark_as_complete()
		case 4:
			return delete_task()
		case 5:
			return exit()


display()