system = [] # list to save large amount of data set
def add_income():
    amount = float(input("Enter income amount: "))
#...........Validation of the amount..............
    while float(amount) <= 0:
        print("Invalid input....")
        print("Enter the income again....")
        amount = float(input("Enter income amount: "))
        
#..............Category input......................
    category = input("Enter category: ")   
    while not category:
        print("Category can't be empty.")
        category = input("Enter category: ")
#..............Date input.......................
    date = input("Enter date (YYYY-MM-DD): ")
    while not date:
        print("Date section can't be left empty.")
        date = input("Enter date (YYYY-MM-DD): ")
#....................Adding to list.............
    system.append({"type":"Income","amount":amount,"category":category,"date":date})
    print("Income added successfully...")

    
#............... Add_Expenses...........
def add_expenses():
    amount = float(input("Enter expense amount: "))
#...........Validation of the amount..............
    while float(amount) <= 0:
        print("Invalid input....")
        print("Enter the expense again....")
        amount = float(input("Enter expense amount: "))
#..............Category input......................
    category = input("Enter category: ")   
    while not category:
        print("Category can't be empty.")
        category = input("Enter category: ")
#..............Date input.......................
    date = input("Enter date (YYYY-MM-DD): ")
    while not date:
        print("Date section can't be left empty.")
        date = input("Enter date (YYYY-MM-DD): ")
#....................Adding to list.............
    system.append({"type":"Expense","amount":amount,"category":category,"date":date})
    print("Expense added successfully...")


    
def trans():
    if not system: # list is empty or no transaction is done
        print("No record found!")
        return
    print("\nType              Amount           Category          Date") #\n will print in next line
    for sys in system:
        print("         ",sys['type'],"        ",sys['amount'],"        ",sys['category'],"        ",sys['date'])
        
def summary():
    total_in = 0 
    total_ex = 0
    for sys in system:
        if sys["type"] == "Income":
            total_in += sys["amount"]
        elif sys["type"] == "Expense":
            total_ex += sys["amount"]
            
    Balance = total_in - total_ex
    
    print("..........Your Account summary...........")
    print("\n Total Income :",total_in)
    print("\n Total Expenses :",total_ex)
    print("\n Available Balance :",Balance)
def menu():
    while True:
        print("--------Welcome to Finanace management system----------")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. Summary")
        print("5. Exit")

        choice = input("Enter value from (1-5) to proceed further: ")
        # The input is valid 
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expenses()
        elif choice == "3":
            trans()
        elif choice == "4":
            summary()
        elif choice == "5":
            print("Thank you for choosing us.....Goodbye!")
            break
        else:
            print("Invalid choice, Please try again.")

menu()
