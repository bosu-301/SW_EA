def omok():
    ppan = [[0]*21]
    omok_p = [[0] + list(map(int, input().split())) + [0] for i in range(19)]
    omok_pan = ppan + omok_p + ppan

    dx = [1, 1, 1, 0] 
    dy = [-1, 1, 0, 1]

    for j in range(1, 20):
        for i in range(1, 20):
            dol = omok_pan[i][j]
            if dol:
                for n in range(4):
                    count = 1
                    x = j
                    y = i

                    while True:
                        if omok_pan[y + dy[n]][x + dx[n]] == omok_pan[i][j]:
                            x += dx[n]
                            y += dy[n]
                            count += 1
                            if count > 5:
                                break
                        else:
                                break
                    if count == 5:
                        if omok_pan[i - dy[n]][j - dx[n]] != dol:
                            print(dol)
                            print(i, j)
                            return
    else:
        print(0)
        return 
omok()