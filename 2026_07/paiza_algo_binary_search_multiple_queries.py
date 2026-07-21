n = int(input())
a = list(map(int,input().split()))
q = int(input())
k = [0] * q

for i in range(q):
    k[i] = int(input())
    left = 0
    right = n - 1
    found = False
    
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == k[i]:
            found = True
            break
        elif a[mid] < k[i]:
            left = mid + 1 
        else:
            right = mid - 1
    if found == True:
        print("Yes")
    else:
        print("No")