a=int(input("how many messages you wants to send"))
for i in range(1,a+1):
    import pywhatkit
    pywhatkit.headless_pyk.sendwhatmsg('no. with country code','hii',20,30)
    print()
    
