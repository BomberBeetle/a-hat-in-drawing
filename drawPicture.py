import math
import sys
import keyboard
import mouse 
import time
from hitherdither import palette 
from hitherdither import ordered 
from PIL import Image

#dictionary "ColorName": (xPos, yPos, (redVal, greenVal, blueVal))

colors = {
    "black" : (190,320,(0,0,0)),
    "white" : (320,320,(255,255,255)),
    "red" : (190,440,(249,79,79)),
    "green": (320,440,(99,249,79)),
    "blue": (190,560,(70,172,207)),
    "yellow": (320,560,(255,207,99)),
    "ltblue": (190,680,(133,243,198)),
    "beige": (320,680,(255,229,194)),
    "brown": (190,800,(172,116,68)),
    "gray": (320,800,(122,119,154)),
    }

hexPalette = [
        0x000000, 0xFFFFFF, 0xF94F4F, 0x63F94F, 0x46ACCF, 0xFFCF63, 0x85F3C6, 0xFFE5C2, 0xAC7444, 0x7A779A
            ]

#The degree of difference between two RGB Values in the form of (Red, Green Blue)
def rgbDiff(a,b):
    rmean = (a[0] + b[0])//2
    r = a[0] - b[0]
    g = a[1] - b[1]
    b = a[2] - b[2]
    return math.sqrt((((512+rmean)*r*r)>>8) + 4*g*g + (((767-rmean)*b*b)>>8))

def getMostSimilar(pixel, colors):
    
    lowestDiff = [sys.maxsize,""]
    
    for key in colors.keys():

            pixelDiff = rgbDiff(pic.getpixel((x,y)) ,colors[key][2])
            
            if pixelDiff < lowestDiff[0]:
                
                lowestDiff[0], lowestDiff[1] = pixelDiff, key

    return lowestDiff

def drawPixel(x,y,color, lastColor):
    if color != lastColor:
        mouse.release()
        mouse.move(colors[color][0]*xResMulti,colors[color][1]*yResMulti)
        time.sleep(0.064)
        mouse.hold()
        time.sleep(0.032)
        mouse.release()
        
    mouse.move(x+5,y+3)
    time.sleep(0.064)
    mouse.hold()
    time.sleep(0.032)
    lastColor = color
    return lastColor

#key of the last color used to draw something
lastColor = None
resString = input("Type the resolution of your game (XResolution x YResolution)").split('x')
xResMulti = int(resString[0])/1920
yResMulti = int(resString[1])/1080
ditheringOrder = 2**int(input("inform the level of dithering (0 is no dithering)\n"))
dithering = (ditheringOrder != 1)

resolutionMultiplier = float(input("please inform the resolution multiplier (default is 53x53, recommended is multiplier is 2.)\n"))

#size of the picture drawn. larger pictures are very slow to draw.
size = (math.floor(53*resolutionMultiplier), math.floor(53*resolutionMultiplier))


unprosPic = Image.open(input("Please inform the name of the file (CaSe SENSitive!)\n"))

pic = unprosPic.convert("RGB").resize(size, Image.ANTIALIAS)
if dithering:
    
    pic = ordered.yliluoma.yliluomas_1_ordered_dithering(pic, palette.Palette(hexPalette), order=ditheringOrder).convert("RGB")


keyPic = []
                
for x in range(0,math.floor(53*resolutionMultiplier)):
    keyPic.insert(x,[])
    for y in range(0,math.floor(53*resolutionMultiplier)):
        mostSimilar = getMostSimilar(pic.getpixel((x,y)),colors)
        if not dithering:
            pic.putpixel((x,y),colors[mostSimilar[1]][2])
        keyPic[x].insert(y,mostSimilar[1])
                                                                                                                              
pic.save("outpic.jpeg", "JPEG")
input("IMAGE PROCESSING COMPLETE. DUMPING MODIFIED PICTURE TO 'outpic.jpeg'. SWITCH TO A HAT IN TIME'S WINDOW and PRESS 'a' TO START (WARNING! SCREEN MUST BE FULLSCREEN!)PRESS 's' AT ANY TIME TO ABORT THE OPERATION.")
test = ("ltblue", "red", "green", "blue","yellow","beige","brown","gray","white","black")
while not keyboard.is_pressed('a'):
    continue


for x in range(0, math.floor(53*resolutionMultiplier)):
    mouse.release()
    for y in range(0,math.floor(53*resolutionMultiplier)):
            
            quit() if keyboard.is_pressed('s') else print("Drawing x{} y{}".format(x,y))
            xPos = math.floor(((x*16)//resolutionMultiplier+540)*xResMulti)
            yPos = math.floor((((y*16)//resolutionMultiplier)+120)*yResMulti)
            lastColor = drawPixel(xPos,yPos,keyPic[x][y],lastColor)
mouse.release()
