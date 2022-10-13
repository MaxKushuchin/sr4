n = int(input())
array = [float(i) for i in input().split()]
mx = 0
for i in range(n):
    if (array[i] >= array[mx]):
        mx = i
for i in range (mx + 1, n):
    array[i] = 0
print(array)