# Логические операторы используются для работы с несколькими условиями

x = 8
y = 12

# and — оба условия должны быть True
print(x > 5 and y > 10)

# or — достаточно одного True
print(x < 5 or y > 10)

# not — инвертирует значение
print(not x == 8)

# Пример из реальной логики
age = 20
has_passport = True

print(age >= 18 and has_passport)
