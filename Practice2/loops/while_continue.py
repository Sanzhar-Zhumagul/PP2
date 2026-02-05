# continue пропускает текущую итерацию

num = 0

while num < 6:
    num += 1
    if num == 3:
        continue
    print(num)
