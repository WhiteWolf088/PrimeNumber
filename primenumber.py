num=int(input("Enter the value boss  :  "))
temp=False
if num>1:
    for i in range(2,num):
        if(num%i==0):
            temp= True
            break
if temp:
    print(num,"Is not prime number")
else:
    print(num,"Is a prime number")
