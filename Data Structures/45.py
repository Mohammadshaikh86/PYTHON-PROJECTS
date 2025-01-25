# Create a dictionary of student grades
grades = {
    "Om": 85,
    "Ben": 92,
    "Shiva": 78,
    "Bankim": 95
}

# Prompt the user for a name
name = input("Enter a student's name: ")

# Display the grade
if name in grades:
    print(f"{name}'s grade is: {grades[name]}")
else:
    print(f"No grade found for {name}")
