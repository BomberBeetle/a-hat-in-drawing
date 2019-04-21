import keyboard
import mouse 
import time
from threading import Thread
from PIL import Image
#dictionary "ColorName": (xPos, yPos, (redVal, greenVal, blueVal))
lastColor = None
resolutionMultiplier = 2
size = (54*resolutionMultiplier, 54*resolutionMultiplier)
unprosPic = Image.open("inpic.jpg")
pic = unprosPic.convert("RGB").resize(size, Image.ANTIALIAS)
for x in pic:
    for y in x:
        print(str(y))
input()
colors = {
    "black" : (320,360,(0,0,0)),
    "white" : (425,360,(255,255,255)),
    "red" : (320,460,(0,0,0)),
    "green": (425,460,(255,255,255)),
    "blue": (320,560,(0,0,0)),
    "yellow": (425,560,(255,255,255)),
    "ltblue": (320,660,(0,0,0)),
    "beige": (425,660,(255,255,255)),
    "brown": (320,760,(0,0,0)),
    "gray": (425,760,(255,255,255)),
    }
test = ("ltblue", "red", "green", "blue","yellow","beige","brown","gray","white","black")
def drawPixel(x,y,color, lastColor):
    if color != lastColor:
        mouse.release()
        mouse.move(colors[color][0],colors[color][1])
        time.sleep(0.032)
        mouse.hold()
        time.sleep(0.032)
        mouse.release()
        
    mouse.move(x+5,y+3)
    time.sleep(0.032)
    mouse.hold()
    time.sleep(0.032)
    lastColor = color
    return lastColor

time.sleep(5)
for x in range(0, 54*resolutionMultiplier):
    mouse.release()
    time.sleep(0.0)
    for y in range(0,54*resolutionMultiplier):
            
            quit() if keyboard.is_pressed('a') else print("Drawing x{} y{}".format(x,y))
            lastColor = drawPixel(((x*13)//resolutionMultiplier)+610,((y*13)//resolutionMultiplier)+202,test[y%10],lastColor)
mouse.release()
