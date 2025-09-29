from abc import ABC, abstractmethod
import json
class Employee(ABC):
    def __init__(self, employee_id: str, name: str, 
    department: str):
        self._employee_id = employee_id
        self._name = name
        self._department = department
    
    @property
    def employee_id(self):
        return self._employee_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def department(self):
        return self._department   
    @department.setter
    def department(self, value):
        self._department = value
    
    @abstractmethod
    def calculate_salary(self) -> float:
        pass
    
    def display_details(self) -> str:
        return f"ID: {self._employee_id}, Name: {self._name}, Dept: {self._department}"
    
    @abstractmethod
    def to_dict(self) -> dict:
        pass

class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, department, 
    monthly_salary):
        super().__init__(employee_id, name, department)
        self._monthly_salary = monthly_salary
    
    @property
    def monthly_salary(self):
        return self._monthly_salary    
    @monthly_salary.setter
    def monthly_salary(self, salary):
        if salary >= 0:
            self._monthly_salary = salary
    
    def calculate_salary(self) -> float:
        return self._monthly_salary
    
    def display_details(self):
        base = super().display_details()
        return f"{base}, Salary: {self._monthly_salary}"
    
    def to_dict(self):
        return {
            "type": "fulltime",
            "employee_id": self._employee_id,
            "name": self._name,
            "department": self._department,
            "monthly_salary": self._monthly_salary
        }

class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, department, 
    hourly_rate, hours_worked_per_month):
        super().__init__(employee_id, name, department)
        self._hourly_rate = hourly_rate
        self._hours_worked_per_month = hours_worked_per_month
    
    @property
    def hourly_rate(self):
        return self._hourly_rate    
    @hourly_rate.setter
    def hourly_rate(self, rate):
        if rate >= 0:
            self._hourly_rate = rate    
    
    @property
    def hours_worked_per_month(self):
        return self._hours_worked_per_month    
    @hours_worked_per_month.setter
    
    def hours_worked_per_month(self, hours):
        if hours >= 0:
            self._hours_worked_per_month = hours
    
    def calculate_salary(self) -> float:
        return self._hourly_rate * self._hours_worked_per_month
    
    def display_details(self):
        base = super().display_details()
        return {base, 
        "Hourly Rate:", self._hourly_rate, 
        "Hours:", self._hours_worked_per_month}
    
    def to_dict(self):
        return {
            "type": "parttime",
            "employee_id": self._employee_id,
            "name": self._name,
            "department": self._department,
            "hourly_rate": self._hourly_rate,
            "hours_worked_per_month": self._hours_worked_per_month
        }

class Manager(FullTimeEmployee):
    def __init__(self, employee_id, name, department, monthly_salary, bonus):
        super().__init__(employee_id, name, department, monthly_salary)
        self._bonus = bonus
    
    @property
    def bonus(self):
        return self._bonus
    @bonus.setter
    def bonus(self, value):
        if value >= 0:
            self._bonus = value
    
    def calculate_salary(self) -> float:
        return super().calculate_salary() + self._bonus
    
    def display_details(self):
        base = super().display_details()
        return f"{base}, Bonus: {self._bonus}"
    
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "manager"
        data["bonus"] = self._bonus
        return data

class Company:
    def __init__(self, data_file='employees.json'):
        self._employees = {}
        self._data_file = data_file
        self._load_data()
    
    def _load_data(self):
        try:
            with open(self._data_file, 'r') as f:
                data = json.load(f)
                for emp in data:
                    e_type = emp['type']
                    if e_type == 'fulltime':
                        obj = FullTimeEmployee(
                        emp['employee_id'], 
                        emp['name'], emp['department'], 
                        emp['monthly_salary'])
                    elif e_type == 'parttime':
                        obj = PartTimeEmployee(
                        emp['employee_id'], 
                        emp['name'], 
                        emp['department'], 
                        emp['hourly_rate'], 
                        emp['hours_worked_per_month'])
                    elif e_type == 'manager':
                        obj = Manager(
                        emp['employee_id'], 
                        emp['name'], 
                        emp['department'], 
                        emp['monthly_salary'], 
                        emp['bonus'])
                    else:
                        continue
                    self._employees[obj.employee_id] = obj
        except FileNotFoundError:
            pass
    def _save_data(self):
        with open(self._data_file, 'w') as f:
            json.dump([e.to_dict() for e in self._employees.values()], f, indent=4)
    def add_employee(self, employee: Employee) -> bool:
        if employee.employee_id in self._employees:
            return False
        self._employees[employee.employee_id] = employee
        self._save_data()
        return True
    def remove_employee(self, employee_id: str) -> bool:
        if employee_id in self._employees:
            del self._employees[employee_id]
            self._save_data()
            return True
        return False
    def find_employee(self, employee_id: str):
        return self._employees.get(employee_id)
    def calculate_total_payroll(self) -> float:
        return sum(emp.calculate_salary() for emp in self._employees.values())
    def display_all_employees(self):
        for emp in self._employees.values():
            print(emp.display_details())
    def generate_payroll_report(self):
        print("Payroll Report:")
        print()
        for emp in self._employees.values():
            print("ID:", emp.employee_id) 
            print("Name:", emp.name) 
            print("Type:", type(emp).__name__) 
            print("Salary:", emp.calculate_salary())
        print()
        print(f"Total Payroll: {self.calculate_total_payroll()}")

def main():
    company = Company()
    while True:
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Remove Employee")
        print("5. Calculate Total Payroll")
        print("6. Generate Payroll Report")
        print("7. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            emp_type = input("Enter type: ").lower()
            eid = input("Enter ID: ")
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            if emp_type == 'fulltime':
                salary = float(input("Enter Monthly Salary: "))
                emp = FullTimeEmployee(eid, name, dept, salary)
            elif emp_type == 'parttime':
                rate = float(input("Enter Hourly Rate: "))
                hours = float(input("Enter Hours Worked: "))
                emp = PartTimeEmployee(eid, name, dept, rate, hours)
            elif emp_type == 'manager':
                salary = float(input("Enter Monthly Salary: "))
                bonus = float(input("Enter Bonus: "))
                emp = Manager(eid, name, dept, salary, bonus)
            else:
                print("Invalid type.")
                continue
            if company.add_employee(emp):
                print("Employee added successfully.")
            else:
                print("Employee ID already exists.")

        elif choice == '2':
            company.display_all_employees()

        elif choice == '3':
            eid = input("Enter Employee ID: ")
            emp = company.find_employee(eid)
            if emp:
                print(emp.display_details())
            else:
                print("Employee not found.")

        elif choice == '4':
            eid = input("Enter Employee ID to remove: ")
            if company.remove_employee(eid):
                print("Employee removed.")
            else:
                print("Employee not found.")

        elif choice == '5':
            print(f"Total Payroll: {company.calculate_total_payroll()}")

        elif choice == '6':
            company.generate_payroll_report()

        elif choice == '7':
            break

        else:
            print("Invalid choice.")

main()