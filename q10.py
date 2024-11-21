#Given a dictionary of student scores, write a function to find the student with the highest score.
students = {"Alice": 85, "Bob": 92, "Charlie": 88}
max_value=max(students.values())
print([name for name,score in students.items() if score==max_value])