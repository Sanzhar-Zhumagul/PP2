"""
LECTURE NOTES
WRITING FILES IN PYTHON

Режимы записи:
'w'  – запись (перезаписывает файл)
'a'  – добавление в конец
'x'  – создание нового файла (ошибка если существует)

Основные методы:
write()     – записывает строку
writelines() – записывает список строк
"""

# запись файла
with open("output.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Python file writing example\n")

# добавление данных
with open("output.txt", "a") as f:
    f.write("This line was appended\n")

# запись списка строк
lines = ["Line1\n", "Line2\n", "Line3\n"]

with open("output2.txt", "w") as f:
    f.writelines(lines)