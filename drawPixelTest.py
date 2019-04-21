import math
import sys
import keyboard
import mouse 
import time
from hitherdither import palette 
from hitherdither import ordered 
from PIL import Image

bayerMap =  [
            [0,35,15],
            [30,25,10],
            [20,5,40],
            ]
#dictionary "ColorName": (xPos, yPos, (redVal, greenVal, blueVal))

colors = {
    "black" : (320,360,(0,0,0)),
    "white" : (425,360,(255,255,255)),
    "red" : (320,460,(249,79,79)),
    "green": (425,460,(99,249,79)),
    "blue": (320,560,(70,172,207)),
    "yellow": (425,560,(255,207,99)),
    "ltblue": (320,660,(133,243,198)),
    "beige": (425,660,(255,229,194)),
    "brown": (320,760,(172,116,68)),
    "gray": (425,760,(122,119,154)),
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

#key of the last color used to draw something
lastColor = None

ditheringOrder = int(input("inform the order of dithering\n"))

resolutionMultiplier = float(input("please inform the resolution multiplier (default is 54x54, recommended is multiplier is 2.)\n"))

#size of the picture drawn. larger pictures are very slow to draw.
size = (math.floor(54*resolutionMultiplier), math.floor(54*resolutionMultiplier))


unprosPic = Image.open(input("Please inform the name of the file (CaSe SENSitive!)\n"))

pic = unprosPic.convert("RGB").resize(size, Image.ANTIALIAS)

pic = ordered.yliluoma.yliluomas_1_ordered_dithering(pic, palette.Palette(hexPalette), order=ditheringOrder).convert("RGB")


keyPic = []
                
for x in range(0,math.floor(54*resolutionMultiplier)):
    keyPic.insert(x,[])
    for y in range(0,math.floor(54*resolutionMultiplier)):
        mostSimilar = getMostSimilar(pic.getpixel((x,y)),colors)      
        keyPic[x].insert(y,mostSimilar[1])
                                                                                                                              
pic.save("outpic.jpeg", "JPEG")
input("IMAGE PROCESSING COMPLETE. DUMPING MODIFIED PICTURE TO 'outpic.jpeg'. AFTER SENDING ANY TEXT, YOU HAVE 30 SECONDS TO SWITCH TO A HAT IN TIME'S WINDOW. PRESS 'a' AT ANY TIME TO ABORT THE OPERATION.")
test = ("ltblue", "red", "green", "blue","yellow","beige","brown","gray","white","black")


time.sleep(30)
for x in range(0, math.floor(54*resolutionMultiplier)):
    mouse.release()
    for y in range(0,math.floor(54*resolutionMultiplier)):
            
            quit() if keyboard.is_pressed('a') else print("Drawing x{} y{}".format(x,y))
            lastColor = drawPixel(((x*13)//resolutionMultiplier)+610,((y*13)//resolutionMultiplier)+202,keyPic[x][y],lastColor)
mouse.release()
