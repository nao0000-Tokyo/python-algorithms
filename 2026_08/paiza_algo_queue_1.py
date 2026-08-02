queue = [""] * 256
queue_front = 0
queue_end = -1

q = int(input())
for i in range(q):
    query = input().split()
    if query[0] == "1":
        queue[queue_end+1] = query[1]
        queue_end += 1
    elif query[0] == "2":
        print(queue[queue_front])
        queue_front += 1
    
    print(*queue[queue_front:queue_end+1])
