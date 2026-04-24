def farenheit(c):
    f=32+ (180/100)*(c)
    return f
def celsius(f):
    c=(f-32)*(100/180)
    return c
choice=float(input("CONVERT 1.Farenheit ----> Celsius or 2.Celsius -----> Farenheit. Choose 1 or 2\n"))
if choice==2:
    c=float(input("Enter temperature in celsius"))
    print(str(farenheit(c))+ "F")
elif choice==1:
    f=float(input("Enter temperature in farenheit"))
    print(str(celsius(f))+"C")
else:
    print("Invalid input")
