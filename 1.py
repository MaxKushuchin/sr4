n = int(input()) #размерность массива
array = [float(i) for i in input().split()] #ввод массива с вещественными значениями в строку
mx = 0
for i in range(n):
    if (array[i] >= array[mx]):
        mx = i 
for i in range (mx + 1, n):
    array[i] = 0
print(array)
