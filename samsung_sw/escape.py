import copy
def move(o_arr,o_d,cnt,o_i):
    if cnt>=11:
        return 99
    r = [-1,1,0,0]
    c = [0,0,-1,1]
    rt_box = []
    for i in range(4):
        if o_i == 4:
            pass
        elif r[i]+r[o_i] == 0 or c[i]+c[o_i] ==0:
            continue
        trg1, trg2 = 0,0
        arr = list(copy.deepcopy(o_arr))
        d = {x: y for x,y in o_d.items()}

        a,b = d['R']
        if arr[a+r[i]][b+c[i]] in '.O':
            a,b = d['R']
            arr[a][b] = '.'
            while arr[a+r[i]][b+c[i]] in '.O':
                d['R'] = [a+r[i],b+c[i]]
                a,b = d['R']
                if arr[a][b] == 'O':
                    trg1 = 1
            if trg1:
                pass
            else:
                arr[a][b] = 'R'

                    
        a,b = d['B']
        if arr[a+r[i]][b+c[i]] in '.O':      
            a,b = d['B']
            arr[a][b] = '.'
            while arr[a+r[i]][b+c[i]] in '.O':
                d['B'] = [a+r[i],b+c[i]]
                a,b = d['B']
                if arr[a][b] == 'O':
                    if cnt == 1:
                        trg2 = 1
                        pass
                    else:
                        return 99
            arr[a][b] = 'B'
        if trg1 and not trg2:
            return cnt
        else :
            rt_box.append(99)

        a,b = d['R']
        if arr[a+r[i]][b+c[i]] in '.O':
            a,b = d['R']
            arr[a][b] = '.'

            while arr[a+r[i]][b+c[i]] == '.':
                d['R'] = [a+r[i],b+c[i]]
                a,b = d['R']
            arr[a][b] = 'R'

        if trg1 and trg2:
            continue

        rt_box.append(move(arr,d,cnt+1,i))
    return min(rt_box)


N, M = list(map(int,input().split()))
arr = [list(input()) for i in range(N)]
d = {}

for i in range(N):
    for j in range(M):
        d[arr[i][j]] = [i,j]
result = move(arr,d,1,4)
if result >11:
    result = -1

print(result)