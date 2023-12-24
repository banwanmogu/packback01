def show(n, x, cost, f,name,rou):
    print('weight=',f[n,x])
    for i in range(n,0,-1):
      if(f[n,x]>f[n-1,x]):
          rou.append(n)
          x=x-cost[n]
          n=n-1
      else:

          n=n-1
    for i in range(0,len(rou)):
        print(name[rou[i]])