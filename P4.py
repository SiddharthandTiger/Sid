a = float(input("Enter 1st Number :-"))

b = float(input("Enter 2nd Number :-"))

c= input("what do you want to do (1st+2nd,1st-2nd,1st*2nd,1st/2nd,1st^2nd,2nd-1st,2nd/1st,2nd^1st) PLEASE WRITE COMPLETELY e.g. if you want to add write'1st+2nd' ")


if(c=='1st+2nd'):

    print(a,'+',b,'=',a+b)


elif(c=='1st-2nd'):

    print(a,'-',b,'=',a-b)


elif(c=='1st*2nd'):
    print(a,'*',b,'=',a*b)


elif(c=='1st/2nd'):

    print(a,'/',b,'=',a/b)


elif(c=='1st^2nd'):
    print(a,'^',b,'=',a**b)


elif(c=='2nd-1st'):

    print(b,'-',a,'=',b-a)


elif(c=='2nd/1st'):

    print(b,'/',a,'=',b/a)


elif(c=='2nd^1st'):

    print(b,'^',a,'=',b**a)

else:
    print("PLEASE ONLY ENTER THE VALID OPERATIONS WHICH ARE GIVEN ABOVE")

    


