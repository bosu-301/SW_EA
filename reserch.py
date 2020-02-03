from itertools import combinations
import copy
def virus_extend(resc):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    trg = 1
    while True:
        for x in range (len(resc)):
            for y in range (len(resc)):
                if resc[x][y] == 2:
                    for I in range(4):	#현재 위치의 상하좌우를 효율적으로 체크하는 코드
                        testX = x+dx[I]
                        testY = y+dy[I]
                        if 0<=testX<len(resc) and 0<=testY<len(resc):
                            if resc[testX][testY] == 0:
                                resc[testX][testY] = 2
                                trg = 0
                if trg == 0:
                    break
            if trg == 0:
                break
        if trg == 1:
            num_safe = 0
            for x in range (len(resc)):
                for y in range (len(resc)):
                    if resc[x][y] ==0:
                        num_safe += 1
            return num_safe
        trg = 1

def make_wall(resc,N,M):
'''    a = N*M
    for x in range (a-2):
        resc_l = []
        for w in resc:
            resc_l += w
        for y in range (x+1,a-1):
            for z in range(y+1,a):
                
                if resc_l[x] == 0:
                    resc_l[x] = 1
                if resc_l[y] == 0:
                    resc_l[y] = 1
                if resc_l[z] == 0:
                    resc_l[z] = 1
                for i in range(N):
                    resc[i] = resc_l[i*M:i*M+M]
    return virus_extend(resc)'''
    nulll = []
    for x in range(N):
        for y in range(M):
            if resc[x][y] == 0:
                nulll += [(x,y)]
    a = combinations(nulll,3)
    for x in a:
        for y in x:
            tmp_resc = copy.deepcopy(resc)
        
            

N, M = list(map(int,input().split()))
resc = [list(map(int,input().split())) for i in range(N)]


print()
print(make_wall(resc,N,M))