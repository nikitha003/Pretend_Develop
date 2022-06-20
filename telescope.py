#This game is based on a telescope getting focussed by the player as soon as it appears. The faster he is, more points he will get.

from tkinter import *
import time
import random

#Creating a window in Tkinter
window = Tk()
window.wm_attributes('-alpha', 0.7)

##Position of spacetelescope

#Position of betelgeuseSupernova
betelgeuseSupernovax = 0

#Number of Supernova
betelgeuseSupernovaCount = 1

count = 0

#Creating a canvas widget
skyCanvas = Canvas(window, width = 2000, height = 1200, bg = "Red")
skyCanvas.pack() #Putting the canvas widget onto the window.

#Putting the sky image onto the canvas
skyImg = PhotoImage(file = "Milky_Way_Arch.png")
skyImage = skyCanvas.create_image(500, 500, image = skyImg)

#Putting the space telescope onto the canvas
telescopeImg = PhotoImage(file = "spaceTelescopeUp.png")
telescopeImage = skyCanvas.create_image(500, 700, image = telescopeImg)

#Putting the Betelgeuse supernova onto the canvas
betelgeuseSupernovaImg = PhotoImage(file = "Betelgeuse_supernova_small(5).png")
betelgeuseSupernovax = random.randint(10, 1200)
betelgeuseSupernovaImage = skyCanvas.create_image(betelgeuseSupernovax, 200, image = betelgeuseSupernovaImg)

def moveRight(event):
    global betelgeuseSupernovaCount
    global betelgeuseSupernovaImg
    global betelgeuseSupernovaImage
    global betelgeuseSupernovax
    global count 
    skyCanvas.move(telescopeImage, 10, 0)
    deleted = 0
    count = count + 1

    #betelgeuseSupernovaCount  = betelgeuseSupernovaCount + 1
    #print("betelgeuseSupernovaCount: " + betelgeuseSupernovaCount)
    print("count : " + str(count))

    deleteRanNumber = random.randint(10, 12000)#Some Number
    print(str(deleteRanNumber))
    
    #if deleteRanNumber <= 7000 and betelgeuseSupernovaCount > 10:
    if deleteRanNumber <= 7000 and count > 10: 
        skyCanvas.delete(betelgeuseSupernovaImage)
        betelgeuseSupernovaCount = random.randint(10, 30)
        print("betelgeuseSupernovaCount: " + str(betelgeuseSupernovaCount))
        deleted = 1


    #if deleteRanNumber > 10:
    #if deleted, means immediately another supernova has to be created
    if deleted:
        count = 0
        #betelgeuseSupernovaCount = 0
        betelgeuseSupernovax = random.randint(10, 1000)
        betelgeuseSupernovaImage = skyCanvas.create_image(betelgeuseSupernovax, 300, image = betelgeuseSupernovaImg)
        #betelgeuseSupernovaImage = skyCanvas.create_image(random.randint(10, 1200), 300, image = betelgeuseSupernovaImg)

def moveLeft(event):
    skyCanvas.move(telescopeImage, -10, 0)

#Making the space telescope move
skyCanvas.bind_all("<Right>", moveRight)

"""
print("Here")
deleteRanNumber = random.randint(10, 12000)#Again some number
print(str(deleteRanNumber))
if deleteRanNumber < 8000 and betelgeuseSupernovaCount == 1:
    skyCanvas.delete(betelgeuseSupernovaImage)
    betelgeuseSupernovaCount = betelgeuseSupernovaCount - 1
elif betelgeuseSupernovaCount == 0:
    betelgeuseSupernovaPositionx = random.randint(10, 1200)
    betelgeuseSupernovaImage = skyCanvas.create_image(betelgeuseSupernovax, 300, image = betelgeuseSupernovaImg) 
"""

skyCanvas.bind_all("<Left>", moveLeft)



#Making the supernova disappear
#skyCanvas.delete(betelgeuseSupernovaImage)


print("Before mainloop")
window.mainloop()
