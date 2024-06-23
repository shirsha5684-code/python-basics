'''traffic light=red--->stop,traffic light=yellow--->people go but cars wait,light=green--->go'''
light=input("enter the colour")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
        print("people go but cars wait")
elif(light=="green"):
     print("go")
else:
    print("invalid colour")