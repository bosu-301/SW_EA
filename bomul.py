# def BFS():


import copy
r5 = [[1]*5]*5
r4 = [[1]*4]*4
r3 = [[1]*3]*3
r2 = [[1]*2]*2
r1 = [[1]*1]*1

r = [r1,r2,r3,r4,r5]

o_arr = [list(map(int, input().split())) for i in range(10)]
num_1 = 0
for i in o_arr:
    num_1 += sum(i)

result = []
a = []
for p in range(5,0,-1):
    arr = copy.deepcopy(o_arr)
    a.append(p)
    cnt = 0
    # print(a)
    # print()
    # for q in arr:
    #     print(*q)
    # print()

    for r_num in range(4, -1, -1):
        if r_num in a:
            continue
        # print()
        # for q in arr:
        #     print(*q)
        # print()

        for i in range(10-r_num):
            for j in range(10-r_num):
                if arr[i][j]:
                    new = []
                    for k in range(i,i+r_num+1):
                        new.append(arr[k][j:j+r_num+1])
                    if new == r[r_num]:

                        # print()
                        # for q in arr:
                        #     print(*q)
                        # print()

                        cnt += 1
                        for k in range(i, i + r_num + 1):
                            arr[k][j:j + r_num + 1] = [0]*(r_num+1)
    # print()
    # for q in arr:
    #     print(*q)
    # print()

    result.append(cnt)
print(result)
