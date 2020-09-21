# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:59:28 2020

@author: Administrator
"""

while True:
    try:
        n, v = map(int, raw_input().split())
        wi = []
        vi = []
        answer = []
        for i in range(n):
            ti, pi = map(int, raw_input().split())
            wi.append(ti)
            vi.append(pi)
        #如果2倍所有的糖果的数量小于卡车体积，则说明最优解为全部糖果
        if n*2<v:
            lis=[]
            for i in range(1, n+1):
                lis.append(str(i))
            print(sum(vi))
            print(' '.join(lis))
        else:
            va = [[0 for j in range(v + 1)] for i in range(n + 1)]
            for i in range(0, n + 1):
                va[i][0] = 0
            for j in range(1, v + 1):
                va[0][j] = 0
            for i in range(1, n + 1):
                for j in range(1, v + 1):
                    if j < wi[i - 1]:
                        va[i][j] = va[i - 1][j]
                    else:
                        va[i][j] = max(va[i - 1][j], va[i - 1][j - wi[i - 1]] + vi[i - 1])
            if v == 0 or n == 0 or va[n][v]==0:
                print('0')
                print("No")
            else:
                print(va[n][v])
                for i in range(n, 0, -1):
                    if va[i][v] != va[i - 1][v] and va[i][v] == (va[i - 1][v - wi[i - 1]] + vi[i - 1]):
                        answer.append(i)
                        v = v - wi[i - 1]
                    else:
                        continue
                for i in range(0, len(answer)):
                    answer[i] = str(answer[i])
                answer = answer[::-1]
                print(" ".join(answer))
    except ValueError:
        break