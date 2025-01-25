class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Example usage
student = Student("Alice", "12345")
student.add_grade(85)
student.add_grade(90)
student.add_grade(88)
print(f"Average grade: {student.average_grade():.2f}")
