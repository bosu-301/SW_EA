import copy

t = int(input())
for tc in range(1,1+t):
    N = int(input())
    arr = [list(map(int,input().split()))for i in range(N)]

    stair = []
    man = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 1:
                stair.append([i,j,arr[i][j]])
            elif arr[i][j] == 1:
                man.append([i,j])
    for i in range(len(man)):
        man[i].append(abs(stair[0][0] - man[i][0]) + abs(stair[0][1] - man[i][1]))
        man[i].append(abs(stair[1][0] - man[i][0]) + abs(stair[1][1] - man[i][1]))

    ar = [0]*len(man)
    sub_arr = [[0]*len(man)]
    while True:
        for i in range(len(man)-1,-1,-1):
            if ar[i] == 1:
                ar[i] = 0
            else :
                ar[i] = 1
                sub_arr.append(copy.copy(ar))
                break
        if ar.count(1) == len(man):
            break

    min_ = []
    for sub in sub_arr:
        st1_q, st2_q = [], []
        for i in range(len(man)):
            if sub[i]:
                st1_q.append(man[i][2]+stair[0][2])
            else:
                st2_q.append(man[i][3]+stair[1][2])
        st1_q.sort()
        st2_q.sort()

        for i in range(len(st1_q)-3):
            if stair[0][2]+st1_q[i]-st1_q[i+3]>0:
               st1_q[i+3]=stair[0][2]+st1_q[i]
        for i in range(len(st2_q)-3):
            if stair[1][2]+st2_q[i]-st2_q[i+3]>0:
                st2_q[i+3]=stair[1][2]+st2_q[i]
        
        if len(st1_q) == 0:
            min_.append(st2_q[-1])
        elif len(st2_q) == 0:
            min_.append(st1_q[-1])
        else:
            min_.append(max(copy.deepcopy(st1_q[-1]),copy.deepcopy(st2_q[-1])))

    print(f'#{tc} {min(min_)+1}')