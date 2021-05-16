a=int(input("Enter no."))
sum =0
while(a>0):
    sum=sum+a%10
    a=a//10
print("Sum of digits=",sum)    
