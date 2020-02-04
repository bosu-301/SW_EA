from itertools import combinations
import copy
import sys
#sys.stdin = open("input.txt", "r")

def virus_extend(resc,N,M):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    trg = 1
    while True:
        for x in range (N):
            for y in range (M):
                if resc[x][y] == 2:
                    for I in range(4):	#현재 위치의 상하좌우를 효율적으로 체크하는 코드
                        testX = x+dx[I]
                        testY = y+dy[I]
                        if 0<=testX<N and 0<=testY<M:
                            if resc[testX][testY] == 0:
                                resc[testX][testY] = 2
                                trg = 0
        if trg == 1:
            num_safe = 0
            for x in range (N):
                for y in range (M):
                    if resc[x][y] ==0:
                        num_safe += 1
            return num_safe
        trg = 1

def make_wall(resc,N,M):

    nulll = []
    for x in range(N):
        for y in range(M):
            if resc[x][y] == 0:
                nulll += [(x,y)]
    com_a = combinations(nulll,3)

    cnt = 0
    for i in com_a:
        tmp_resc = copy.deepcopy(resc)
        tmp_resc[i[0][0]][i[0][1]] = 1
        tmp_resc[i[1][0]][i[1][1]] = 1
        tmp_resc[i[2][0]][i[2][1]] = 1
        a = virus_extend(tmp_resc,N,M)
        if cnt < a:
            cnt = a
    return cnt



N, M = list(map(int,input().split()))
resc = [list(map(int,input().split())) for i in range(N)]


print(make_wall(resc,N,M))