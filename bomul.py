import copy

def mk_combination(n, o_com, i):
    if i == -1:
        if n == 0:
            return [(len(o_com), o_com)]
        else:
            return

    p = 1
    return_box = []
    tmp = copy.copy(o_com)
    
    a_3 = mk_combination(n, tmp, i-1)
    if a_3:
        return_box += mk_combination(n, tmp, i-1)

    while n>= (i+1)**2 and p <=5:
        com = copy.copy(o_com)
        for s in range(p):
            com.append(i)
        n -= (i+1)**2
        if i == 0:
            if n == 0:
                a_1 = mk_combination(n, com, i-1)
                if a_1:
                    return_box += a_1
        else:
            a_2 = mk_combination(n, com, i-1)
            if a_2:
                return_box += a_2
        p += 1
    
    return return_box


def bomul():
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
    combinations = mk_combination(num_1, [], 4)
    combinations.sort()

    if num_1 == 0:
        print(0)
        return
    # print(combinations)

    result = -1


    for case in combinations:
        arr = copy.deepcopy(o_arr)
        trg = 1
        for r_num in case[1]:
            trg = 1

            for i in range(10-r_num):
                for j in range(10-r_num):
                    if arr[i][j]:
                        new = []
                        for k in range(i,i+r_num+1):
                            new.append(arr[k][j:j+r_num+1])
                        if new == r[r_num]:
                            trg = 0
                            for k in range(i, i + r_num + 1):
                                arr[k][j:j + r_num + 1] = [0]*(r_num+1)
                    if not trg:
                        break
                if not trg:
                    break
            if trg:
                break
        if trg:
            continue
        result = case[0]
        break
        # print()
        # for q in arr:
        #     print(*q)
        # print()
    print(result)

bomul()