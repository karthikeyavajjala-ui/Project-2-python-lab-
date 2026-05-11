class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    def show_details(self):
        print("Name:", self.name)
        print("ID:", self.emp_id)
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department
    def show_details(self):
        super().show_details()
        print("Department:", self.department)
emp = Employee("John", 101)
mgr = Manager("Alice", 102, "HR")
emp.show_details()
print()
mgr.show_details()