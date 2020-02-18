from itertools import product
import copy

def clear(a,dx,dy,arr,n):
    for k in range(n-1):
        for i in range(n):
            for j in range(n):                
                x = ((1-dx[a])//2)*(n-1) + ((dx[a]+1)//2*2 + (dx[a]+1)%2*2-1)*i
                y = ((1-dy[a])//2)*(n-1) + ((dy[a]+1)//2*2 + (dy[a]+1)%2*2-1)*j
                if 0<=y+dy[a]<n and 0<= x+dx[a] <n:
                    if arr[y+dy[a]][x+dx[a]] == 0:
                        new = arr[y+dy[a]][x+dx[a]]
                        arr[y+dy[a]][x+dx[a]] = arr[y][x]
                        arr[y][x] = new
def move(arr,go,n):
    dx,dy,arrow = [1,-1,0,0],[0,0,1,-1],[0,1,2,3]
    dx1,dy1 = [-1,1,0,0],[0,0,-1,1]
    a = arrow.index(go)
    clear(a,dx,dy,arr,n)

    for i in range(n):
        for j in range(n):
            x = ((1-dx1[a])//2)*(n-1) + ((dx1[a]+1)//2*2 + (dx1[a]+1)%2*2-1)*i
            y = ((1-dy1[a])//2)*(n-1) + ((dy1[a]+1)//2*2 + (dy1[a]+1)%2*2-1)*j
            if 0<=y+dy1[a]<n and 0<= x+dx1[a] <n:
                if arr[y+dy1[a]][x+dx1[a]] == arr[y][x]:
                    arr[y][x]*=2
                    arr[y+dy1[a]][x+dx1[a]] = 0
    clear(a,dx,dy,arr,n)
    tmp = []

    for x in arr:
        tmp += x
    return(max(tmp))
    

def choo2048():

    N = int(input())
    arr = [list(map(int,input().split())) for i in range(N)]
    t = [0,1,2,3]
    try_set = list(product(t,repeat=5))
    result = []
    for _set in try_set:
        new = copy.deepcopy(arr)
        a=0
        for gogo in _set:
            a = move(new,gogo,N)
        result.append(a)

    print(max(result))

choo2048()