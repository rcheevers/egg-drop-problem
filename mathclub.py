lis = [0,1,2]

for x in range(3,1001):
    minn = x*2
    for a in range(1,x):
        minn = min(1+max(a-1,lis[x-a]),minn)
    y = minn
    
    lis += [y]
    print(x,": ",y)
