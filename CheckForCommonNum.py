s1=[1,4,7,2,9,6,3,0,4,8]
s2=[1,4,5,1,11,7,2,19,6,3,10,4,8]
L1=[]
map={}
count=0
print(s1)
print(s2)
for i in s1:
    count=0
    for e in s2:
        if i==e:
            count+=1
            map[i]=count
L1.append(map)
print(L1)
print(map.keys(),"showed",map.values(),"times in these two sets")