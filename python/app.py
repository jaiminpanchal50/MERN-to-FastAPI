# variables are container for storing data values
# in js we declare variables using var,let and const but in python we declare variables by simply assigning a value to a name
# there are no keywords for declaring variables in python like let or const

name = "  Jaimn   " #string
age = 23 #number
experince = 2.5 #number float
is_married = False #boolean

# print(len(name))
# print(name[-3])
# print(name[0:3])
# print(name.upper())
# print(name.capitalize())
# print(name.lower())
# print(name.title())
# print(name.strip())
# print(name.rstrip())
# print(name.lstrip())
# print(name.islower())

# print("jai" in name)
# print("jaiii" not in name)


# if age > 18:
#     print('now you can drink coke')
# elif age > 15:
#     print('you can drink fruit juice')
# else:
#     print("you can drink MILK")



# with ternary operator

message = "you can drink coke " if age > 18 else "you can drink milk"

# print(message)

# function in python is defined using the def keyword

def greet(name):
    print(f"Hello {name}")

# greet('jaimin')


def greet_return(name):
    return f"hii {name}"


message = greet_return("jaimin panchal")
# print(f"message ---> {message}")


# Calculator 


def calculator():
    operation = input("what type of operation do you want to perform >> ")
    num1=int(input('Enter number >>> '))
    num2=int(input('Enter number >>> '))

    if operation == 'sum' or operation == '+':
        print(F"total {num1 + num2}")
    elif operation == 'sub' or operation == '-':
        print(f"answer is {num1 - num2}")
    elif operation == "mul" or operation == '*':
        print(f"answer {num1 * num2}")
    else:
        print(f"answer {num1 / num2}")




# calculator()


# subject Grade system

def subject_grade():
    subject1= input("Enter subject name and marks >>> ")
    subject2= input("Enter subject name and marks >>> ")
    subject3= input("Enter subject name and marks >>> ")
    subject4= input("Enter subject name and marks >>> ")
    subject5= input("Enter subject name and marks >>> ")

    total =int(subject1)+int(subject2)+int(subject3)+int(subject4)+int(subject5)

    percentage = total/500*100

    if percentage >= 90:
        grade ="Grade A"
    elif percentage >= 80:
        grade ="Grade B"
    elif percentage >= 70:
        grade ="Grade C"
    elif percentage >= 60:
        grade ="Grade D"
    else:
        grade ="Grade F"

    print(f"total marks {total}")
    print(f"percentage {percentage}%")
    print(f"Grade {grade}")


# subject_grade()


# Contact book


# def contact_book():
#     contacts=[]
#     add_new = True
#     while add_new:
#         def add_contact():
#             name = input("Enter contact name >>> ")
#             number =int(input("Enter contact number >>> "))
            
#             new_contact={
#                 "name":name,
#                 "number":number
#             }

#             contacts.append(new_contact)   

#         add_another_contact = input(f"Do you want to add more contact Yes/No >>> ")

#         if not add_another_contact:
#             add_new = False


#     def view_contact():
#         for contact in contacts:
#             print(f"Contacts \n {contact}")

#     def remove_contact():
#         name = input("Enter the name >>> ")
        
#         for contact in contacts:
#             if contact['name'] == name:
#                 contacts.remove(contact)
#                 print(f"{name} removed from contact book")
#                 break
#             else:
#                 print("Contact not found")

#     def update_contact():
#         name = input("Enter the name of the contact to update >>> ")
#         new_number = int(input("Enter new number >>> "))

#         for contact in contacts:
#             if contact['name'] == name:
#                 if not contact['number'] == new_number: 
#                     contact['number'] = new_number
#                     print(f"contact updated successfully {contact}")
#                 else:
#                     print(f"Please Enter new number:)")
#                     update_contact()
#             else:
#                 print(f"Contact not found")


#     add_contact()
#     print("*" * 15)
#     view_contact()
#     print("*" * 15)
#     remove_contact()
#     update_contact()


# contact_book()

def add_contact(contacts):
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")

    # Check duplicate
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact already exists!")
            return

    contacts.append({
        "name": name,
        "number": number
    })

    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")

    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Number: {contact['number']}")
        print("-" * 20)


def search_contact(contacts):
    name = input("Enter contact name to search: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\nContact Found")
            print(contact)
            return

    print("Contact not found.")


def update_contact(contacts):
    name = input("Enter contact name to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():

            new_number = input("Enter new number: ")

            if contact["number"] == new_number:
                print("Old and new numbers are the same.")
                return

            contact["number"] = new_number
            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter contact name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


def contact_book():
    contacts = []

    while True:

        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# contact_book()

def add_expense(expenses):
    title=input("Enter Title >> ").strip()
    amount = int(input("Enter amount you spend >> "))

    if not title or amount == 0:
        print(f"Please enter valid title or amount")
        return


    expense = {
        "title":title,
        "amount":amount
    }

    expenses.append(expense)
    
    print("New Expense added successfully")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expense List ---")

    for expense in expenses:
        print(f"Title: {expense['title']}")
        print(f"Amount: {expense['amount']}")
        print("-" * 20)

def search_expenses(expenses):
    print("-" * 20)
    title = input("Enter title >>> ").strip()
    amount = int(input("Enter amount >>> "))

    if not title or amount == 0:
        print("Please Enter Valid Title or Amount:)")
        return
    
    for expense in expenses:
        if expense['title'].lower() == title.lower() or expense['amount'] == amount:
            print("\n--- Expense List ---")            
            print("\nExpense Found")
            print(expense)
            return
        else:
            print("Not Found ")

def update_expenses(expenses):
    print("-" * 20)
    title = input("Enter title >>> ").strip()

    for expense in expenses:
        if expense['title'].lower() == title.lower():
            print("Expense Found")
            print(expense)
            new_amount = int(input("Enter new amount >>> "))
            if not new_amount:
                print("Please enter valid amount")
                return

            if expense['amount'] == new_amount:
                print("Old and new amount are same")
                return

            expense['amount'] = new_amount
            print("Expense updated successfully")
            return
        else:
            print("Expense not found")

def delete_expenses(expenses):
    print("-" * 20)
    title = input("Enter title >>> ").strip()

    for expense in expenses:
        if expense['title'].lower() == title.lower():
            print("Expense Found")
            print(expense)
            expenses.remove(expense)
            print("Expense deleted successfully")
            return
        else:
            print("Expense not found")

def expenses_tracker():
    expenses=[]

    while True:

        print("\n===== CONTACT BOOK =====")
        print("1. Add expense")
        print("2. View expense")
        print("3. Search expense")
        print("4. Update expense")
        print("5. Delete expense")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            search_expenses(expenses)

        elif choice == "4":
            update_expenses(expenses)

        elif choice == "5":
            delete_expenses(expenses)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

expenses_tracker()