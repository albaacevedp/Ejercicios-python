arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

dim = len(arr)
n1 = n2 = 0
for i in range(dim):
    n1 += arr[i][i]
    n2 += arr[i][dim-i-1]

res = abs(n1-n2)
print(res)
# resultado=abs(n1-n2)

# Comparison Sorting, hacer una lista con
arr = [1, 1, 3, 2, 1]
result = 5*[0]
for i in arr:
    result[i] += 1
print(result)

for i in range(5):
    print(i**2)
