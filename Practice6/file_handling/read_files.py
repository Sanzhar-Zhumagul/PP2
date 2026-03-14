"""
LECTURE NOTES
READING FILES IN PYTHON

Основные способы чтения файлов:
1. open() – открывает файл
2. read() – читает весь файл
3. readline() – читает одну строку
4. readlines() – читает все строки в список
5. with open() – безопасный способ работы с файлами (автоматически закрывает файл)

Режимы открытия файла:
'r'  – чтение
'rb' – чтение в бинарном режиме
"""

# пример чтения всего файла
f = open("example.txt", "r")
content = f.read()
print(content)
f.close()

# чтение по строке
f = open("example.txt", "r")
line = f.readline()
print(line)
f.close()

# чтение всех строк
f = open("example.txt", "r")
lines = f.readlines()
print(lines)
f.close()

# лучший способ — with
with open("example.txt", "r") as f:
    data = f.read()
    print(data)