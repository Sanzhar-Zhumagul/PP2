"""
LECTURE NOTES
WORKING WITH DIRECTORIES

Модуль os позволяет:
создавать папки
удалять папки
получать список файлов

Основные функции:
os.mkdir()   – создать папку
os.listdir() – список файлов
os.getcwd()  – текущая директория
"""

import os

# текущая директория
print("Current directory:", os.getcwd())

# создание папки
os.mkdir("test_directory")

# список файлов
files = os.listdir()

print("Files and directories:")
for f in files:
    print(f)