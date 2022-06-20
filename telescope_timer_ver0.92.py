#This game is based on a telescope getting focussed by the player as soon as it appears. The faster he is, more points he will get.
#References
#Instructions

from tkinter import *
import time
import random
import pickle #To store/persist and recover python objects/data

#Creating a window in Tkinter
window = Tk()
window.title("Supernova Hunter")

#Creating the Starting label

##Position of spacetelescope
spaceTelescopeX = 0
spaceTelescopeY = 0

#Position of betelgeuseSupernova
betelgeuseSupernovax = 0

#Number of Supernova
betelgeuseSupernovaCount = 1

#Game Over Flag
gameOver = 0

count = 0
delete = 1

#Score of the player
score = 0 

#For debugging
debug = 1

#Positions of asteroids
psycheX = 200
psycheY = 200

vestaX = 500
vestaY = 200

pallasX = 800
pallasY = 200

player_name = " "

#Dictionary to store player's name and the associated score
player_dict = {}

#Game Start Control
gameStart = 0

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

#Putting the asteroid onto the canvas
vestaImg = PhotoImage(file = "Vesta.png")
vestaImage = skyCanvas.create_image(vestaX, vestaY, image = vestaImg)

#Putting the asteroid onto the canvas
pallasImg = PhotoImage(file = "Pallas.png")
pallasImage = skyCanvas.create_image(100, 800, image = pallasImg)

def collisionDetectionVesta():
    global gameStart
    if gameStart:
        global telescopeImage
        global vestaImage
        global gameOver
        telescopeBB = skyCanvas.bbox(telescopeImage)
        vestaBB = skyCanvas.bbox(vestaImage)
        #print(telescopeBB[0])
        #print(vestaBB[2])
        """
        if telescopeBB[0] < vestaBB[2] < telescopeBB[2] and telescopeBB[1] < vestaBB[3] < telescopeBB[3]:
            skyCanvas.delete(telescopeImage)
            gameStart = 0
            print("After deleting Telescope gameStart = " + str( gameStart))
        """
        #if vestaBB[3] > telescopeBB[3] and vestaBB[2] > telescopeBB[2]:
        #    skyCanvas.delete(telescopeImage)
        #    gameStart = 0

#Vesta Animation
def vestaAppear():
    global vestaImg
    global vestaImage
    global vestaX
    global vestaY
    global score
    skyCanvas.delete(vestaImage)
    #If Vesta reaches the bottom, its placement is reset by the below if statement block
    if vestaY > 900:
        #vestaY = 10
        vestaY = random.randint(10, 500)
        vestaX = random.randint(10, 1200)
    vestaY = vestaY + 10
    #The below if conditions makes the game complicated and faster for the player to prgress when the score 
    #goes above a certain threshold. Only the y co-ordinate is controlled
    if score > 200 and score < 400:
        vestaY = vestaY + 10
    if score > 400 and score < 600:
        vestaY = vestaY + 30
    if score > 600 and score > 800:
        vestaY = vestaY + 40
    #The x co-ordinate is set by caling random
    vestaX = vestaX + random.randint(10, 90) 
    vestaImage = skyCanvas.create_image(vestaX, vestaY, image = vestaImg)
    #Calling vestaAppear again onto itself for animation
    skyCanvas.after(100, vestaAppear)
    collisionDetectionVesta()

def pallasAppear():
    global score
    if score > 800:
        global pallasImg
        global pallasImage
        global pallasX
        global pallasY
        skyCanvas.delete(pallasImage)
        if pallasY > 900:
            pallasY = random.randint(10, 500)
            pallasX = random.randint(10, 1200)
        pallasY = pallasY + 30
        pallasX = pallasX + random.randint(10, 90)
        pallasImage = skyCanvas.create_image(pallasX, pallasY, image = pallasImg)
        skyCanvas.after(100, pallasAppear)



#The below method will make the betelgeuseSuppernova to appear in random
def appear():
    global delete
    global betelgeuseSupernovaImage
    global betelgeuseSupernovaImg
    global betelgeuseSupernovax
    print("Inside Appear")
    print("Delete : " + str(delete))
    betelgeuseSupernovax = random.randint(100, 1000)
    
    if delete:
        skyCanvas.delete(betelgeuseSupernovaImage)
        #delete = 0
        betelgeuseSupernovaImage = skyCanvas.create_image(betelgeuseSupernovax, 200, image = betelgeuseSupernovaImg)
        skyCanvas.after(5000, appear)
        #betelgeuseSupernovaImage = skyCanvas.create_image(betelgeuseSupernovax, 200, image = betelgeuseSupernovaImg)
        delete = 1
    




def moveRight(event):
    global betelgeuseSupernovaCount
    global betelgeuseSupernovaImg
    global betelgeuseSupernovaImage
    global betelgeuseSupernovax
    global count
    global score
    global gameStart
    skyCanvas.move(telescopeImage, 10, 0)
    telescopeBB = skyCanvas.bbox(telescopeImage) #Local telescopeBB
    betelgeuseSupernovaBB = skyCanvas.bbox(betelgeuseSupernovaImage)
    #For debugging
    if debug:
        skyCanvas.create_line((telescopeBB[2] + telescopeBB[0])/2,telescopeBB[1], (betelgeuseSupernovaBB[2] + betelgeuseSupernovaBB[0])/2, betelgeuseSupernovaBB[1])
    slopeY = telescopeBB[1] - betelgeuseSupernovaBB[3]
    slopeX = ((telescopeBB[2] + telescopeBB[0])/2) - ((betelgeuseSupernovaBB[2]+ betelgeuseSupernovaBB[0]/2))
    slopeTelescopeBetelgeuseSupernova = slopeY/slopeX

    if slopeTelescopeBetelgeuseSupernova < -0.57 and slopeTelescopeBetelgeuseSupernova > -0.58 and gameStart:#-0.6:
        score = score + 10
        print("Score : " + str(score)) 
        score_label.config(text = "Score " + str(score), font = ("Arial", 20))
    print("SlopeX :" + str(slopeX) + " " + "SlopeY :" + str(slopeY) + " " + "Slope: " + str(slopeTelescopeBetelgeuseSupernova))


    """
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
"""


def moveLeft(event):
    global betelgeuseSupernovaImage
    global score

    skyCanvas.move(telescopeImage, -10, 0)

    telescopeBB = skyCanvas.bbox(telescopeImage) #Local telescopeBB
    betelgeuseSupernovaBB = skyCanvas.bbox(betelgeuseSupernovaImage)

    #For debugging
    if debug:
        skyCanvas.create_line((telescopeBB[2] + telescopeBB[0])/2,telescopeBB[1], (betelgeuseSupernovaBB[2] + betelgeuseSupernovaBB[0])/2, betelgeuseSupernovaBB[1])
    slopeY = telescopeBB[1] - betelgeuseSupernovaBB[3]
    slopeX = ((telescopeBB[2] + telescopeBB[0])/2) - ((betelgeuseSupernovaBB[2]+ betelgeuseSupernovaBB[0]/2))
    slopeTelescopeBetelgeuseSupernova = slopeY/slopeX
    if slopeTelescopeBetelgeuseSupernova < -0.57 and slopeTelescopeBetelgeuseSupernova > -0.58 and gameStart:#-0.6:
        score = score + 10
        print("Score : " + str(score)) 
        score_label.config(text = "Score " + str(score), font = ("Arial", 20))

    print("SlopeX :" + str(slopeX) + " " + "SlopeY :" + str(slopeY) + " " + "Slope: " + str(slopeTelescopeBetelgeuseSupernova))

def betelgeuseSupernovaAppear():
    betelgeuseSupernovax = random.randint(10, 1200)
    betelgeuseSupernovaImage = skyCanvas.create_image(betelgeuseSupernovax, 200, image = betelgeuseSupernovaImg)

#betelgeuseSupernovaImage.after(2000, betelgeuseSupernovaAppear)

#start button command
def start():
    global gameStart
    global player_name
    global player_dict
    global score
    gameStart = 1

    player_name_entry = player_entry.get()
    pickle_recover = open("player_dict.pickle", "rb")#Pickle database/file is opened in read and binary mode
    player_dict = pickle.load(pickle_recover)
    score = player_dict[player_name_entry]
    score_label.config(text = "Score " + str(score), font = ("Arial", 20))

    start_button.config(text = "Started", font = ("Arial", 20))

    if debug:
        print("From Start gameStart : " + str(gameStart))
        print("From Start Name : " + player_name + " " + "Score" + " " + str(score))

def stop():
    global gameStart
    global player_name
    global score
    global player_dict
    gameStart = 0
    #player_name_entry = ""
    start_button.config(text = "Restart", font = ("Arial", 20))

    #Adding elements or updating player_dict and pickle the data
    player_name_entry = player_entry.get()

    player_dict[player_name_entry] = score
    #Pickling
    pickling_data = open("player_dict.pickle", "wb") #opening a pickling file called player_dict.pickle in write and binary mode
    pickle.dump(player_dict, pickling_data)
    pickling_data.close()

    if debug:
        print("From Stop gameStart : " + str(gameStart))
        print("Player Name: " + player_name_entry)
        print("Game Dictionary : ", player_dict)
        print("Testing pickle")
        pickle_recover = open("player_dict.pickle", "rb")
        player_dict = pickle.load(pickle_recover)
        print("From Stop player_dict : " + str(player_dict))
        print("From Stop player name from pickle dict : " + str(player_dict[player_name_entry]))

#Placing the score on the screen

score_label = Label(skyCanvas, text = "Score " + str(score), bg = "black", fg = "white", font = ("Arial", 20))
score_label.place(x = 1770, y = 100)

#Placing the start button
start_button = Button(skyCanvas, text = "Start", bg = "black", fg = "white", font = ("Arial", 20), command = start)
start_button.place(x= 1770, y = 150)

#Placing the stop button
stop_button = Button(skyCanvas, text = "Stop", bg = "black", fg = "white", font = ("Arial", 20), command = stop)
stop_button.place(x= 1770, y = 200)

#Player Name Entry Label
player_label = Label(skyCanvas, text = "Name", font = ("Arial", 20), bg = "black", fg = "white")
player_label.place(x = 1600, y = 750)

#Player name entry box
player_name = ""
player_entry = Entry(skyCanvas, textvariable = player_name, fg = "white", bg = "black", font = ("Arial", 20))
player_entry.place(x = 1600, y = 800)


#Making the space telescope move
skyCanvas.bind_all("<Right>", moveRight)
skyCanvas.bind_all("<Left>", moveLeft)
skyCanvas.after(5000, appear)
skyCanvas.after(1000, vestaAppear)
skyCanvas.after(1000, pallasAppear)

print("Before mainloop")
window.mainloop()
