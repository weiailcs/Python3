import random
import matplotlib.pyplot as plt
import numpy as np


# 函数模拟点的随机掉落，并分为两组
def check(tmp):
    global ans, ansX, ansY
    global inX, inY
    global outX, outY

    tmpX = random.random()
    tmpY = random.random()
    if (tmpX ** 2 + tmpY ** 2) <= 1:
        ans = ans + 1
        inX = np.append(inX, tmpX)
        inY = np.append(inY, tmpY)
    else:
        outX = np.append(outX, tmpX)
        outY = np.append(outY, tmpY)
    ansX = np.append(ansX, tmp)
    ansY = np.append(ansY, float(ans / tmp * 4))


# 变量声明
ans = 0;
inX = np.array([])
inY = np.array([])
outX = np.array([])
outY = np.array([])
ansX = np.array([])
ansY = np.array([])
circleX = np.linspace(0, 1, 10000)
circleY = (1 - circleX ** 2) ** (0.5)

# 主体
# N = int(input("循环次数: "))
N = 1000
for i in range(N):
    check(i + 1)

fig = plt.figure()
p1 = fig.add_subplot(121)
p2 = fig.add_subplot(122)
# i行j列，一维顺序下的第k个

p1.axis("square")
p1.axis([0.0, 1.0, 0.0, 1.0])
p1.scatter(inX, inY, c="r", marker=".")
p1.scatter(outX, outY, c="b", marker=".")
p1.plot(circleX, circleY, 'r')

p2.plot(ansX, ansY)

# 结果输出
plt.show()
print(format(float(ans / N * 4), "0.6f"))
