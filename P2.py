a=float(input("Enter 1st Number "))

b=float(input("Enter 2nd Number "))

c=float(input("Enter 3rd Number "))


if(a>b):
    if(a>c):
        if(b>c):
            print(a,'>',b,'>',c)
        elif(c>b):
            print(a,'>',c,'>',b)
        elif(b==c):
            print(a,'>(',b,'=',c,')')
    elif(c>a):
        print(c,'>',a,'>',b)
    elif(c==a):
        print('(',a,'=',c,')>',b)
        
    
elif(b>a):
    if(b>c):
        if(a>c):
            print(b,'>',a,'>',c)
        elif(c>a):
            print(b,'>',c,'>',a)
        elif(a==c):
            print(b,'>(',a,'=',c,')')
    elif(c>b):
        print(c,'>',b,'>',a)
    elif(c==b):
        print('(',b,'=',c,')>',a)
            
    
elif(c>a):
    if(c>b):
        if(a>b):
            print(c,'>',a,'>',b)
        elif(b>a):
            print(c,'>',b,'>',a)
        elif(b==a):
            print(c,'>(',a,'=',b,')')
    elif(b>c):
        print(b,'>',c,'>',a)
    elif(b==c):
        print('(',b,'=',c,')>',a)

else:
    print(a,'=',b,'=',c)
        
        
        
