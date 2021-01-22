median=[9,1,7,3,1,5,0]
number2=len(median)
for t in range(number2-1):        #sort
    for g in range(number2-t-1):
        print(t,g)
        next=g+1
        if median[next]<median[g]:
            tmp=median[next]
            median[next]=median[g]
            median[g]=tmp
            print(median)