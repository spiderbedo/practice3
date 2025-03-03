x, y, n = input().split()
r = int(n) * int(x) + (int(y) * int(n)) // 100
k = (int(y) * int(n)) % 100
print(r, "руб.", k, "коп.")

