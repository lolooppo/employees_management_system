"""
Employee Management System
Author: Alaa Omran
Date: 2025-08-19

Description:
This program provides a simple employee management system with a
command-line interface. It allows the user to:
  - Add new employees
  - List all employees
  - Delete employees within a given age range
  - Update an employee's salary by name
  - Exit the program

The system is structured into three main classes:
  - Employee: Represents an employee with name, age, and salary.
  - EmployeesManager: Manages a collection of employees and provides
    methods to add, list, remove, and update employees.
  - FrontendManager: Handles user interaction through menus and
    delegates operations to the EmployeesManager.
"""



class Employee:
    """
    Represents an employee with a name, age, and salary.
    Provides getter and setter methods for each attribute,
    and a string representation of the employee.
    """

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return "\tEmployee: {0} has age {1} and salary {2}".format(self.name, self.age, self.salary)


class EmployeesManager:
    """
    Manages a collection of Employee objects.

    Provides methods to:
      - Add a new employee
      - List all employees
      - Remove employees within a given age range
      - Update an employee's salary by name
    """

    def __init__(self):
        self.employees = []

    def addEmployee(self, employee):
        self.employees.append(employee)

    def listEmployees(self):
        return self.employees

    def removeEmployeeByAgeRange(self, rangeStart, rangeEnd):
        deleted_employees = []
        for i in range(len(self.employees) - 1, -1, -1):
            if rangeStart <= self.employees[i].age <= rangeEnd:
                deleted_employees.append(self.employees[i].name)
                self.employees.pop(i)
        return deleted_employees

    def updateEmployeeSalary(self, name, new_salary):
        employee_found = False
        for employee in self.employees:
            if employee.name == name:
                employee.salary = new_salary
                employee_found = True
                break
        return employee_found

class FrontendManager:
    """
    Handles the user interface for managing employees.

    Provides methods to:
      - Display a menu of choices
      - Add a new employee via user input
      - List all employees
      - Delete employees within a given age range
      - Update an employee's salary by name
      - Run the interactive employee management system
    """

    def __init__(self, choices):
        self.employeesManager = EmployeesManager()
        self.choices = choices

    def mainMenu(self):
        for idx, choice in enumerate(self.choices):
            print(idx+1, ") ", choice)

        user_choice = -1
        while user_choice < 1 or user_choice > len(self.choices):
            user_choice = int(input("Select a choice(from {0} to {1}): ".format(1, len(self.choices))))

        return user_choice

    def addEmployee(self):
        print("Enter employee data: ")
        new_employee_name = input("\tEnter the name: ")
        new_employee_age = int(input("\tEnter the age: "))
        new_employee_salary = float(input("\tEnter the salary: "))
        new_employee = Employee(new_employee_name, new_employee_age, new_employee_salary)
        self.employeesManager.addEmployee(new_employee)

    def listEmployees(self):
        employees = self.employeesManager.listEmployees()
        if not employees:
            print("\t**No employees found**")
            return
        print("**Employees List**")
        for employee in employees:
            print(employee)

    def deleteByAge(self):
        from_age = int(input("\tEnter age from: "))
        to_age = int(input("\tEnter age to: "))
        deleted_employees = self.employeesManager.removeEmployeeByAgeRange(from_age, to_age)
        for employee in deleted_employees:
            print("\tDeleting {}".format(employee))

    def updateSalary(self):
        name = input("\tEnter name: ")
        new_salary = float(input("\tEnter new salary: "))
        is_updated = self.employeesManager.updateEmployeeSalary(name, new_salary)
        if not is_updated:
            print("\t**Employee not found**")

    def run_system(self):
        while True:
            choice = self.mainMenu()
            if choice == 1:
                self.addEmployee()
            elif choice == 2:
                self.listEmployees()
            elif choice == 3:
                self.deleteByAge()
            elif choice == 4:
                self.updateSalary()
            else:
                print("\t\tBYE")
                break


if __name__ == "__main__":
    manager = FrontendManager(["Add a new employee", "List all employees", "Delete by age range", "Update salary given a name", "End the program"])
    manager.run_system()