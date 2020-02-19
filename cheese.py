r,c = list(map(int,input().split()))
arr = [list(map(int,input().split())) for i in range(r)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

arr[0][0] = 2
stack = [(0,0)]
while stack:
    i,j = stack.pop()
    for n in range(4):
        if 0 <= i+dr[n] < r and 0 <= j+dc[n] < c:
            if arr[i+dr[n]][j+dc[n]] == 0:
                arr[i+dr[n]][j+dc[n]] = 2
                stack.append((i+dr[n],j+dc[n]))

start = 2
while True:
    for i in range(r):
        for j in range(c):
            if arr[i][j] == start:
                for n in range(4):
                    if 0 <= i+dr[n] < r and 0 <= j+dc[n] < c:
                        if arr[i+dr[n]][j+dc[n]] == 1:
                            arr[i+dr[n]][j+dc[n]] = start + 1

    for x in arr:
        if 1 in x:
            break
    else:
        break

    for i in range(r):
        for j in range(c):
            if arr[i][j] == start+1:
                for n in range(4):
                    if 0 <= i+dr[n] < r and 0 <= j+dc[n] < c:
                        if arr[i+dr[n]][j+dc[n]] == 0:
                            arr[i+dr[n]][j+dc[n]] = start+1
                            stack = [(i+dr[n],j+dc[n])]
                            while stack:
                                i,j = stack.pop()
                                for n in range(4):
                                    if 0 <= i+dr[n] < r and 0 <= j+dc[n] < c:
                                        if arr[i+dr[n]][j+dc[n]] == 0:
                                            arr[i+dr[n]][j+dc[n]] = start + 1 
                                            stack.append((i+dr[n],j+dc[n]))

    start += 1

left = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == start + 1:
            left += 1
print(start-1)
print(left)


    