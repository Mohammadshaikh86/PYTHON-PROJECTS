class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, id, salary, department):
        super().__init__(name, id, salary)
        self.department = department

    def get_salary(self):
        return self.salary + 1000  # Manager bonus

# Example usage
emp = Employee("John Doe", "E001", 50000)
mgr = Manager("Jane Smith", "M001", 60000, "IT")

print(f"Employee salary: ${emp.get_salary()}")
print(f"Manager salary: ${mgr.get_salary()}")
