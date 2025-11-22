import numpy as np

with open('points.txt') as f:
    lines = f.readlines()

    Xzahyou = np.array([])
    Yzahyou = np.array([])

    for line in lines:
        A = line.split(',')
        x = float(A[0])
        y = float(A[1])
        Xzahyou = np.append(Xzahyou, x)
        Yzahyou = np.append(Yzahyou, y)

    Xheikin = Xzahyou.mean()
    Yheikin = Yzahyou.mean()

    kosuu = len(Xzahyou)

    bunshi = 0
    bunbo = 0

    for i in range(kosuu):
        bunshi += (Xzahyou[i] - Xheikin) * (Yzahyou[i] - Yheikin)
        bunbo  += (Xzahyou[i] - Xheikin) ** 2

    b = bunshi / bunbo
    a = Yheikin - b * Xheikin

    print(a)
    print(b)


