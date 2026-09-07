def add_new_employee(data: list):
    name = input("Type in the employee's name: ")
    ident = int(input("Type in the employee's ID: "))
    depart_number = int(input("Type in the department number: "))
    age = int(input("Type in employee's age: "))
    data.append([name, ident, depart_number, age])
    print("Added a new employee")

def display(data: list):
    print(f"{"Name":<20}{"ID":<10}{"Department Number":<11}{"Age"}")
    for employee in data:
        print(f"{employee[0]:<20}{employee[1]:<10}{employee[2]:<11}{employee[3]}")

def search_by_name(data: list, name):
    '''
    The function execute the search by name
    '''
    result = []
    for employee in data:
        if employee[0] == name:
            result.append(employee)
    display(result)

def display_by_age(data: list):
    '''
    Display all employees' information in chronological order by age.
    '''
    temp_data = data.copy()
    temp_data.sort(key=lambda employee: employee[3])
    print("Employees' information in chronological order by age.")
    display(temp_data)

def remove_by_id(data, ID: int):
    '''
    Remove the employee by ID
    '''
    for ind in range(len(data)):
        if data[ind][1] == ID:
            data.pop(ind)
            print(f"Remove ID {ID} successfully")
            break

def main():
    data = [
        ["Duong Anh Nguyen", 1001, 10, 35],
        ["Khoi Duong", 1002, 20, 22],
        ["Ken Chueng", 1003, 30, 28],
        ["Tom Nguyen", 1004, 10, 41],
        ["Jensen Huang", 1005, 10, 55],
        ["Duong Anh Nguyen", 1006, 20, 50]
    ]

    while True:

        print("\nEmployee management system")
        print("1. Enter a new employee's information")
        print("2. Display all employees' information")
        print("3. Find employee's information by name")
        print("4. Display all employees' information in chronological order by age.")
        print("5. Remove the employee by ID")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_employee(data)

        elif choice == "2":
            display(data)

        elif choice == "3":
            name = input("Type in the employee's name: ")
            search_by_name(data, name)

        elif choice == "4":
            display_by_age(data)

        elif choice == "5":
            ID = int(input("Type in the employee's ID: "))
            remove_by_id(data, ID)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()