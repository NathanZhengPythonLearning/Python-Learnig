import sys

number=int(input("Please inout the number that will be factorized: "))
for i in range(1,number+1):
    for j in range(i,number+1):
        if i*j==number:
            print(i,"and",j,"is a factor")
    