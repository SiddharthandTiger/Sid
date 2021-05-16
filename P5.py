a= float(input("Enter your height 'ONLY NUMERICAL VALUE':-"))

b= input("Enter your height unit (i.e. the value you have given above is in  cm or m or              feets or inches):-")

c= float(input("enter your weight in KG:-"))


if(b=='cm'):

    print('your BMI is',c/((a/100)**2))


elif(b=='m'):

    print('your BMI is',c/(a**2))


elif(b=='feets'):

    print('your BMI is',c/((a*0.3048)**2))


elif(b=='inches'):

    print('your BMI is',c/((a*0.0254)**2))


else:

    print("Only give value in the units which are given above")
