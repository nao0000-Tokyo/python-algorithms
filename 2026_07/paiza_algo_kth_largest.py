# Repeatedly find the maximum value using linear search until reaching the k-th largest element.
n = int(input())
a = list(map(int,input().split()))
k = int(input())
maximum = -1000000000
k_maximum = -1000000000

for i in range(k-1):
    for j in range(len(a)):
        if a[j] > maximum:
            maximum = a[j]
    a.remove(maximum)
    maximum = -1000000000

for i in a:
    if i > k_maximum:
        k_maximum = i
print(k_maximum)