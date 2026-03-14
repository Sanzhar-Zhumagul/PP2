"""
LECTURE NOTES
COPYING AND DELETING FILES

Модули:
os      – работа с операционной системой
shutil  – операции копирования файлов

Функции:
shutil.copy()  – копирование файла
os.remove()    – удаление файла
os.path.exists() – проверка существования файла
"""

import os
import shutil

# копирование файла
shutil.copy("source.txt", "copy.txt")

print("File copied")

# удаление файла
file_name = "copy.txt"

if os.path.exists(file_name):
    os.remove(file_name)
    print("File deleted")
else:
    print("File does not exist")