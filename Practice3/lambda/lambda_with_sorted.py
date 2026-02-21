students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Сортировка по оценке
sorted_students = sorted(students, key=lambda student: student["grade"])

if __name__ == "__main__":
    for student in sorted_students:
        print(student)