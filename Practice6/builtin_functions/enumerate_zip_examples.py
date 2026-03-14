"""
LECTURE NOTES
ENUMERATE AND ZIP

enumerate() – добавляет индекс к элементам
zip() – объединяет несколько списков

Часто используется в циклах.
"""

# enumerate example
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# zip example
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(name, score)

# zip to dictionary
student_scores = dict(zip(names, scores))
print(student_scores)