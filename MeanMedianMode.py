hi=input("Please type which do you want to pick mean,median or mode? ")
if hi=="mean" or hi=="Mean":
    mean=[]
    number=(int(input("Please tpye how many numbers your going to type in: ")))
    for i in range(0,number,1):
        mean.append(int(input("now please type the numbers you want to find out the mean of: ")))
    length=len(mean)
    # print(length)
    # print(mean)
    total=0    
    for i in mean:
        total=total+int(i)  
    TheMeanOfYourNumberIs=total/length
    print(f'{TheMeanOfYourNumberIs=}')
elif hi=="median" or hi=="Median":
    median=[]
    number2=(int(input("Please type how many numbers your going to type in: ")))
    for e in range(0,number2,1):
        median.append(int(input("now please type the numbers you want to find out the median of: ")))
        
    length2=len(median)
    # median=[9,1,7,3,1,5,0]
    # number2=len(median)
    for t in range(number2-1):        #sort
        for g in range(number2-t-1):
            # print(t,g)
            next=g+1
            if median[g]>median[next]:
                tmp=median[next]
                median[next]=median[g]
                median[g]=tmp
                print(median)
            
    if length2%2==1:
        almstdne=length2//2
        print("The median of that str is",median[almstdne])
    elif length2%2==0:
        almstdne2=length2//2-1
        almstdne3=length2//2
        total=(median[almstdne2]+median[almstdne3])/2
        print("the median of that str is",total)
elif hi=="mode" or hi=="Mode":
    mode=[]
    number3=(int(input("Please tpye how many numbers your going to type in: ")))
    for i in range(0,number3,1):
        mode.append(int(input("now please type the numbers you want to find out the mode of: ")))
    length=len(mode)
    for b in range(number3):
        for k in range(b+1,number3):
            if mode[b]>mode[k]:
                tmp=mode[b]
                mode[b]=mode[k]
                mode[k]=tmp
                print(mode)
    # find the number of occurence for every items
    current=0
    map={}
    count=1
    for k in range(1,length):#see how many or first num
        if mode[k]==mode[current]:  
            count+=1
        else:
            b=mode[current]#replace num and map equals how many
            map[b]=count    
            count=1
            current=k
        if k==length-1:
            map[mode[k]]=count
    print(map)

    # get the mode of list---2 steps
    valuesList=list(map.values())
    print(valuesList)
    max=valuesList[0]
    # step 1: get the max of values
    for v in valuesList:
        if max<v:
            max=v
    # step 2: get the keys of max
    modes=[]
    for (k,v) in map.items():
        if v==max:
            modes.append(k)
    print("The mode(s) of your str is ",modes)
    print("The number showed ",map[modes[0]]," times in that str")

else:
    print("Invalid Word!")
        

    
    