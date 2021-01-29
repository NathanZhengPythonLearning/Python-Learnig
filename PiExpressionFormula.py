stop=int(input("Type when you want to stop: "))
i=0
result=0
while True:
    i+=1
    result+=((-1)**(1+i))/((2*i)-1)
    print(result*4)
    if i==stop:
        print(result*4)
        break