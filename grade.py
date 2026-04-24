num=int(input("Enter the number of subjects"))
marks=[]
for i in range(1,num+1):
    marks.append(float(input(f"MARKS {i}:")))
avg=sum(marks)/num
if avg>=90 and avg<=100:
    grade='A'
elif avg>=80 and avg<=89:
    grade='B'
elif avg>=70 and avg<=79:
    grade='C'
elif avg>=60 and avg<=69:
    grade='D'
elif avg>=50 and avg<=59:
    grade='E'
elif avg<50:
    grade='F'
print(f"Average marks={avg:.2f}")
print("Grade:",grade)