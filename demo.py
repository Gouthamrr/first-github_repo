import time 
a=time.strftime('%H:%M:%S')
print(a)
a=int(input("enter the time in 24h format"))
if(a>=12 and a<16):
    print("happy morning")
elif(a>=16 and a<=20):
    print("happy evening")
else:
 print("lazy")
 