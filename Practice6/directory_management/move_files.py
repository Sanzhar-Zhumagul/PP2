"""
LECTURE NOTES
MOVING FILES

Для перемещения файлов используется shutil.move()

Формат:
shutil.move(source, destination)
"""

import shutil
import os

source = "example.txt"
destination = "test_directory/example.txt"

if os.path.exists(source):
    shutil.move(source, destination)
    print("File moved")
else:
    print("Source file not found")