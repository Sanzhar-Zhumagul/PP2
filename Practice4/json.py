#.  Сериализация
import json

data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)
#.  Десериализация
obj = json.loads(json_str)
#.  Работа с файлами
#Запись
with open("data.json", "w") as f:
    json.dump(data, f)
#Чтение
with open("data.json") as f:
    data = json.load(f)
#.    Полезные параметры
json.dumps(data, indent=4)
json.dumps(data, ensure_ascii=False)
json.dumps(data, sort_keys=True)
#.   Кастомные объекты
class User:
    def __init__(self, name):
        self.name = name

def custom_serializer(obj):
    if isinstance(obj, User):
        return {"name": obj.name}
    raise TypeError()
user ="Adam"
json.dumps(user, default=custom_serializer)