a = int(input(" enter number "))
b=input("what do you want to display")
for i in range(1,a+1):
    for j in range(1,a-i+1):
            print(" ",end="")
    for k in range(1,2*i):
            print(b,end="")
    print("")
