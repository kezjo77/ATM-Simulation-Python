print("1.EVEN/ODD CHECKER \n 2.PRIME CHECKER,CHOOSE 1 OR 2")
choice=int(input())
num=int(input("Enter number"))
ch=0
if choice==1:
    if num%2==0:
        print(f"{num} is a even number")
    else:
        print(f"{num} is a odd number")
elif choice==2:
    for i in range(1,num+1):
        if num%i==0:
            ch+=1
    if ch==2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
