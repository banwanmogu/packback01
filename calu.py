import numpy as np



# costlist=[0,34,34,9,18]
# value=[0,508,510,129,217]
# skilllist=['名称', '大胃王', '圆弧艺术家', '顺时针', '弯道加速']
#
# skillnumber= len(skilllist) - 1
# skillpoint=80
# print(skilllist)
# print(costlist)
# print(value)
# f = np.zeros([skillnumber + 1, skillpoint + 1], dtype=int)
# rou=[]
# for i in range(1, skillnumber + 1):
#     for j in range(1, skillpoint + 1):
#         if costlist[i]>j:
#             f[i,j]=f[i-1,j]
#         else:
#             #f[i,j]=max(f[i-1,j],f[i-1,j-cost[i]]+value[i])
#             temp= f[i - 1, j - costlist[i]] + value[i]
#             if(f[i-1,j]>temp):
#                 f[i, j]=f[i-1,j]
#             else:
#                 f[i, j]=temp

def calu(skilllist,costlist,value,skillpoint):   #技能名称列表，技能消耗列表，技能价值列表，技能点数
    skillnumber = len(skilllist) - 1 #技能数
    print('技能列表：',skilllist)
    print('技能所花费：',costlist)
    print('技能的评估价值：',value)
    f = np.zeros([skillnumber + 1, skillpoint + 1], dtype=int)
    rou = []
    for i in range(1, skillnumber + 1):
        for j in range(1, skillpoint + 1):
            if costlist[i] > j:
                f[i, j] = f[i - 1, j]
            else:
                # f[i,j]=max(f[i-1,j],f[i-1,j-cost[i]]+value[i])
                temp = f[i - 1, j - costlist[i]] + value[i]
                if (f[i - 1, j] > temp):
                    f[i, j] = f[i - 1, j]
                else:
                    f[i, j] = temp
    print(f)

    def show(n, x, cost, f, name, rou):
        print('weight=', f[n, x])
        for i in range(n, 0, -1):
            if (f[n, x] > f[n - 1, x]):
                rou.append(n)
                x = x - cost[n]
                n = n - 1
            else:

                n = n - 1
        for i in range(0, len(rou)):
            print(name[rou[i]])

    show(skillnumber, skillpoint, costlist, f, skilllist, rou)
