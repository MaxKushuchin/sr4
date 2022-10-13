x = int(input()) #размерность 1-го массива
z = int(input()) #размерность 2-го массива
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = set() #массив, в котором будут храниться элементы, общие для массивов а и b
for i in range(x):
    for j in range(z):
        if a[i] == b[j]:
            c.add(a[i])
v = ' '.join(map(str, c)) #массив преобразуем в строку с пробелами, чтобы соответсвтовать шаблону вывода в задании
print(v)
