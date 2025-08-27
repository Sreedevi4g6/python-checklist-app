##### create an empty list to store tasks and there status
check_list=[]
def add_task():
    task=input("Enter a task:")
    check_list.append({"Task": task, "Status":"pending"})
    print("New Task Added successfully!!\n")
#Function to view task
def view_task():
    print("your do list: ")
    if len(check_list) == 0:
       print("No pending task!")
    else:
      for index.task in enumerate(check_list,1):
           check_list.append({"task": task, "status": "pending"})
    print("\n")
#Function to remove a task
def remove_task():
   if len(check_list) == 0:
      print("List is empty!")
   else:
    try:
        search_index=int(input("Enter the task number that you want to remove:"))-1
        if 0 <= search_index < len(check_list):
           remove_task = checklist.pop(search_index)
           print(f"Task Removed:{removed_task[task]}")
        else:
           print("Invalid Task number.")
    except valueError:
          print("please Enter a valid Task number.")
#Function to mark a task as done
def mark_done():
   if len(check_list) == 0:
      print("List is empty!")
   else:
       try:
          search_index = int(input("Enter the task number that you want to mark as complete: ")) - 1
          if 0 <= search_index < len(check_list):
             check_list[search_index]['status'] = 'done'
             print(f"Task: {check_list[search_index]['task']} has been marked as Done.")
          else:
             print("Invalid Task number.")
       except ValueError:
             print("Please Enter a valid Task number.")
#Function  to display a menu
def menu():
    while(True):
        print("***main menu***")
        print("1.Add a new task")
        print("2.view All task")
        print("3.remove a task")
        print("4.Mark a task as completed")
        print("5.Exist")

        choice=input("Enter your choice:")
        if choice == "1":
           add_task()
        elif choice == "2":
           view_task()
        elif choice == "3":
           remove_task()
        elif choice == "4":
           mark_done()
        elif choice == "5":
          print("Exiting the application...")
          exit()
        else:
          print("Invalid Choice! Try again!!!")
menu()
