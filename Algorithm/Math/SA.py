import random

# 搜索算法4：模拟退火算法
# 参数：T代表原始温度，cool代表冷却率，step代表每次选择临近解的变化范围
# 原理：退火算法以一个问题的随机解开始，用一个变量表示温度，这一温度开始时非常高，而后逐步降低
# 在每一次迭代期间，算啊会随机选中题解中的某个数字，然后朝某个方向变化。如果新的成本值更
# 低，则新的题解将会变成当前题解，这与爬山法类似。不过，如果成本值更高的话，则新的题解仍
# 有可能成为当前题解，这是避免局部极小值问题的一种尝试。
# 注意：算法总会接受一个更优的解，而且在退火的开始阶段会接受较差的解，随着退火的不断进行，算法
# 原来越不能接受较差的解，直到最后，它只能接受更优的解。
# 算法接受较差解的概率 P = exp[-(highcost-lowcost)/temperature]
def annealingoptimize(self, domain, T=10000.0, cool=0.98, step=1):
    # 随机初始化值
    vec = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]

    # 循环
    while T > 0.1:
        # 选择一个索引值
        i = random.randint(0, len(domain) - 1)
        # 选择一个改变索引值的方向
        c = random.randint(-step, step)  # -1 or 0 or 1
        # 构造新的解
        vecb = vec[:]
        vecb[i] += c
        if vecb[i] < domain[i][0]:  # 判断越界情况
            vecb[i] = domain[i][0]
        if vecb[i] > domain[i][1]:
            vecb[i] = domain[i][1]

        # 计算当前成本和新的成本
        cost1 = self.schedulecost(vec)
        cost2 = self.schedulecost(vecb)

        # 判断新的解是否优于原始解 或者 算法将以一定概率接受较差的解
        if cost2 < cost1 or random.random() < math.exp(-(cost2 - cost1) / T):
            vec = vecb

        T = T * cool  # 温度冷却
        print
        vecb[:], "代价:", self.schedulecost(vecb)

    self.printschedule(vec)
    print
    "模拟退火算法得到的最小代价是：", self.schedulecost(vec)
    return vec
