import math
list1=[]
list2=[]
count=0
total=0
hi=int(input("Please type how many numbers are you going to put in: "))
for i in range(hi):
    hi2=int(input("Please type the first number here and the second on later etc.: "))
    list1.append(hi2)
for e in range(len(list1)):
    count=count+list1[e]#mean
mean=count/len(list1)#mean
# print(mean)
for k in range(len(list1)):
    minmean=(list1[k]-mean)*(list1[k]-mean)#square of dev
    list2.append(minmean)#append into list2
# print(minmean)
# print(list2)
for j in range(len(list2)):
    total+=list2[j]#add up list2[]
mean2=math.sqrt(total/len(list2))#mean again and sqrt
print(mean2)
# print(math.sqrt(2))