#This game is based on a telescope getting focussed by the player as soon as it appears. The faster he is, more points he will get.
#References
#https://commons.wikimedia.org/wiki/File:Betelgeuse_supernova.png
#https://commons.wikimedia.org/wiki/File:Milky_Way_Arch.jpg
#https://commons.wikimedia.org/wiki/File:Hubble_2009_close-up.jpg
#https://commons.wikimedia.org/wiki/File:Pallas_asteroid.png
#https://solarsystem.nasa.gov/resources/415/vesta-sizes-up/

#Instructions --> left and arrow keys are used to move the telescope. Once the supernova is focussed, the player gets credit.
#When the score becomes higher the asteroids become faster and the game becomes much more complicated.
#camel to underscore
#pickle db unavailability
#key unavailability
#deleting redundant variables
#debug level change
#collision detection switching ON

from tkinter import *
import time
import random
import pickle #To store/persist and recover python objects/data
import sys

#Creating a window in Tkinter
window = Tk()
window.title("Supernova Hunter")

#Creating the Starting label

##Position of spacetelescope
#spaceTelescopeX = 0
#spaceTelescopeY = 0

#Position of betelgeuse_supernova
betelgeuse_supernova_x = 0

#Number of Supernova
#betelgeuse_supernova_count = 1

#Game Over Flag
game_over = 0

count = 0
delete = 1

#Score of the player
score = 0 

#For debugging. if 1 means debugging print statements will be printed
debug = 0

#Positions of asteroids
vesta_x = 500
vesta_y = 200

pallas_x = 800
pallas_y = 200

player_name = " "

#Dictionary to store player's name and the associated score
player_dict = {}
player_dict_str = ""#To place the dictionary data into a string

#Game Start Control
game_start = 0

#Creating a canvas widget
sky_canvas = Canvas(window, width = 2000, height = 1200, bg = "Red")
sky_canvas.pack() #Putting the canvas widget onto the window.

#Putting the sky image onto the canvas
sky_img = PhotoImage(file = "Milky_Way_Arch.png")
sky_image = sky_canvas.create_image(500, 500, image = sky_img)

#Putting the space telescope onto the canvas
telescope_img = PhotoImage(file = "spaceTelescopeUp.png")
telescope_image = sky_canvas.create_image(500, 700, image = telescope_img)

#Putting the Betelgeuse supernova onto the canvas
betelgeuse_supernova_img = PhotoImage(file = "Betelgeuse_supernova_small(5).png")
betelgeuse_supernova_x = random.randint(10, 1200)
betelgeuse_supernova_image = sky_canvas.create_image(betelgeuse_supernova_x, 200, image = betelgeuse_supernova_img)

#Putting the asteroid onto the canvas
vesta_img = PhotoImage(file = "Vesta.png")
vesta_image = sky_canvas.create_image(vesta_x, vesta_y, image = vesta_img)

#Putting the asteroid onto the canvas
pallas_img = PhotoImage(file = "Pallas.png")
pallas_image = sky_canvas.create_image(100, 800, image = pallas_img)

def collisionDetectionVesta():
    global game_start
    if game_start:
        global telescope_image
        global vesta_image
        global game_over
        telescope_bb = sky_canvas.bbox(telescope_image)
        vesta_bb = sky_canvas.bbox(vesta_image)
        #print(telescope_bb[0])
        #print(vesta_bb[2])
        if telescope_bb[0] < vesta_bb[2] < telescope_bb[2] and telescope_bb[1] < vesta_bb[3] < telescope_bb[3]:
            sky_canvas.delete(telescope_image)
            stop()
            sys.exit()
        #if vesta_bb[3] > telescope_bb[3] and vesta_bb[2] > telescope_bb[2]:
        #    sky_canvas.delete(telescope_image)
        #    game_start = 0

#Vesta Animation
def vesta_appear():
    global vesta_img
    global vesta_image
    global vesta_x
    global vesta_y
    global score
    sky_canvas.delete(vesta_image)
    if debug:
        print("inside vesta_appear " + str(score))
    #If Vesta reaches the bottom, its placement is reset by the below if statement block
    if vesta_y > 900:
        #vesta_y = 10
        vesta_y = random.randint(10, 500)
        vesta_x = random.randint(10, 1200)
    vesta_y = vesta_y + 10
    #The below if conditions makes the game complicated and faster for the player to prgress when the score 
    #goes above a certain threshold. Only the y co-ordinate is controlled
    if score > 200 and score < 400:
        vesta_y = vesta_y + 10
    if score > 400 and score < 600:
        vesta_y = vesta_y + 30
    if score > 600 and score > 800:
        vesta_y = vesta_y + 40
    #The x co-ordinate is set by calling random
    vesta_x = vesta_x + random.randint(10, 90) 
    vesta_image = sky_canvas.create_image(vesta_x, vesta_y, image = vesta_img)
    #Calling vesta_appear again onto itself for animation
    sky_canvas.after(100, vesta_appear)
    collisionDetectionVesta()

def pallas_appear():
    global score
    global player_dict
    global pallas_img
    global pallas_image
    global pallas_x
    global pallas_y
    player_name_entry = player_entry.get()
    
    if debug:
        print("Inside pallas_appear Player name entry: " + player_name_entry)
        print("Inside pallas_appear Score  " + str(score))
    
    sky_canvas.delete(pallas_image)
    if pallas_y > 900:
        pallas_y = random.randint(10, 500)
        pallas_x = random.randint(10, 1200)
    pallas_y = pallas_y + 10
    pallas_x = pallas_x + random.randint(10, 90)
    pallas_image = sky_canvas.create_image(pallas_x, pallas_y, image = pallas_img)
    sky_canvas.after(100, pallas_appear)
    if score > 200:
        print("Score above 200 : " + str(score))
        pallas_y = pallas_y + 40 #Adding above 30
    collision_detection_pallas()

def collision_detection_pallas():
    global game_start
    if game_start:
        global telescope_image
        global pallas_image
        global game_over
        telescope_bb = sky_canvas.bbox(telescope_image)
        pallas_bb = sky_canvas.bbox(pallas_image)
        #print(telescope_bb[0])
        #print(vesta_bb[2])
        if telescope_bb[0] < pallas_bb[2] < telescope_bb[2] and telescope_bb[1] < pallas_bb[3] < telescope_bb[3]:
            sky_canvas.delete(telescope_image)
            stop()
            sys.exit()


#The below method will make the betelgeuseSuppernova to appear in random
def appear():
    global delete
    global betelgeuse_supernova_image
    global betelgeuse_supernova_img
    global betelgeuse_supernova_x
    print("Inside Appear")
    print("Delete : " + str(delete))
    betelgeuse_supernova_x = random.randint(100, 1000)
    
    if delete:
        sky_canvas.delete(betelgeuse_supernova_image)
        #delete = 0
        betelgeuse_supernova_image = sky_canvas.create_image(betelgeuse_supernova_x, 200, image = betelgeuse_supernova_img)
        sky_canvas.after(5000, appear)
        #betelgeuse_supernova_image = sky_canvas.create_image(betelgeuse_supernova_x, 200, image = betelgeuse_supernova_img)
        delete = 1

def destroy_start_screen():
    start_label.destroy()
    

def start_screen_appear():
    global start_label
    start_label = Label(sky_canvas, text = "Supernova Hunter\n You have to move the space telescope to capture the Supernova\nThe Game will become progressively difficult as the score goes high\nGame will become faster and the  asteroid will come faster", font = ("Arial", 20), bg = "black", fg = "white")
    start_label.place(x = 500, y = 500)
    sky_canvas.after(10000, destroy_start_screen)

def moveRight(event):
    global betelgeuse_supernova_count
    global betelgeuse_supernova_img
    global betelgeuse_supernova_image
    global betelgeuse_supernova_x
    global count
    global score
    global game_start
    sky_canvas.move(telescope_image, 10, 0)
    telescope_bb = sky_canvas.bbox(telescope_image) #Local telescope_bb
    betelgeuse_supernova_bb = sky_canvas.bbox(betelgeuse_supernova_image)
    #For debugging
    if debug and game_over == 0:
        sky_canvas.create_line((telescope_bb[2] + telescope_bb[0])/2,telescope_bb[1], (betelgeuse_supernova_bb[2] + betelgeuse_supernova_bb[0])/2, betelgeuse_supernova_bb[1])
    if game_over == 0:
        slope_y = telescope_bb[1] - betelgeuse_supernova_bb[3]
        slope_x = ((telescope_bb[2] + telescope_bb[0])/2) - ((betelgeuse_supernova_bb[2]+ betelgeuse_supernova_bb[0]/2))
        slope_telescope_betelgeuse_supernova = slope_y/slope_x

    if slope_telescope_betelgeuse_supernova < -0.57 and slope_telescope_betelgeuse_supernova > -0.58 and game_start:#-0.6:
        score = score + 10
        print("Score : " + str(score)) 
        score_label.config(text = "Score " + str(score), font = ("Arial", 20))

        #Updating the leader board label
        player_name_entry = player_entry.get()
        player_dict[player_name_entry] = score #Updating the entry of the present score for the player_name_entry
        if debug:
            print("Inside move right player_dict : ", str(player_dict))
        player_dict_str = str(player_dict)
        player_dict_str = player_dict_str.replace("{", "")
        player_dict_str = player_dict_str.replace("}", "")
        player_dict_str = player_dict_str.replace(",", "\n")
        leader_label.config(text = "Leader Board\n" + player_dict_str, font = ("Arial", 15))
    print("SlopeX :" + str(slope_x) + " " + "SlopeY :" + str(slope_y) + " " + "Slope: " + str(slope_telescope_betelgeuse_supernova))



def moveLeft(event):
    global betelgeuse_supernova_image
    global score
    global player_dict
    global player_dict_str

    sky_canvas.move(telescope_image, -10, 0)

    telescope_bb = sky_canvas.bbox(telescope_image) #Local telescope_bb
    betelgeuse_supernova_bb = sky_canvas.bbox(betelgeuse_supernova_image)

    #For debugging
    if debug and game_over == 0:
        sky_canvas.create_line((telescope_bb[2] + telescope_bb[0])/2,telescope_bb[1], (betelgeuse_supernova_bb[2] + betelgeuse_supernova_bb[0])/2, betelgeuse_supernova_bb[1])
    if game_over == 0:
        slope_y = telescope_bb[1] - betelgeuse_supernova_bb[3]
        slope_x = ((telescope_bb[2] + telescope_bb[0])/2) - ((betelgeuse_supernova_bb[2]+ betelgeuse_supernova_bb[0]/2))
        slope_telescope_betelgeuse_supernova = slope_y/slope_x
    if slope_telescope_betelgeuse_supernova < -0.57 and slope_telescope_betelgeuse_supernova > -0.58 and game_start:#-0.6:
        score = score + 10
        print("Score : " + str(score)) 
        score_label.config(text = "Score " + str(score), font = ("Arial", 20))
        #Updating the leader board label
        player_name_entry = player_entry.get()
        player_dict[player_name_entry] = score #Updating the entry of the present score for the player_name_entry
        if debug:
            print("Inside move left player_dict : ", str(player_dict))
        player_dict_str = str(player_dict)
        player_dict_str = player_dict_str.replace("{", "")
        player_dict_str = player_dict_str.replace("}", "")
        player_dict_str = player_dict_str.replace(",", "\n")
        leader_label.config(text = "Leader Board\n" + player_dict_str, font = ("Arial", 15))

    #print("SlopeX :" + str(slope_x) + " " + "SlopeY :" + str(slope_y) + " " + "Slope: " + str(slope_telescope_betelgeuse_supernova))
#Cheat code implementation for raising the score by 10

def cheat_score(event):
    global score
    global player_dict
    global player_dict_str
    #Gambling. Score may increase or decrease 
    score_mod = random.randint(-3, 3)
    score = score + score_mod
    print("Score : " + str(score)) 
    score_label.config(text = "Score " + str(score), font = ("Arial", 20))
    #Updating the leader board label
    player_name_entry = player_entry.get()
    player_dict[player_name_entry] = score #Updating the entry of the present score for the player_name_entry
    if debug:
        print("Inside cheat_score player_dict : ", str(player_dict))
    player_dict_str = str(player_dict)
    player_dict_str = player_dict_str.replace("{", "")
    player_dict_str = player_dict_str.replace("}", "")
    player_dict_str = player_dict_str.replace(",", "\n")
    leader_label.config(text = "Leader Board\n" + player_dict_str, font = ("Arial", 15))

def boss_key(event):
    sky_canvas.delete()
    #Putting the boss_key image onto the canvas
    boss_img = PhotoImage(file = "boss_image.png")
    boss_image = sky_canvas.create_image(500, 500, image = boss_img)

def betelgeuse_supernovaAppear():
    betelgeuse_supernova_x = random.randint(10, 1200)
    betelgeuse_supernova_image = sky_canvas.create_image(betelgeuse_supernova_x, 200, image = betelgeuse_supernova_img)

#betelgeuse_supernova_image.after(2000, betelgeuse_supernovaAppear)

#start button command
def start():
    global game_start
    global player_name
    global player_dict
    global player_dict_str
    global score
    game_start = 1

    player_name_entry = player_entry.get()
    #Try block to catch FileNotFoundError
    try:
        pickle_recover = open("player_dict.pickle", "rb")#Pickle database/file is opened in read and binary mode
    except FileNotFoundError:
        print("New pickle file gets created")
        pickle_recover = open("player_dict.pickle", "wb")#New file gets created
        pickle.dump(player_dict, pickle_recover)#So that the created file is not empty and avoids "Ran out of Input" error
        pickle_recover.close() #New file closed since it was opened for writing which is not the intention here, but to create a new file
        pickle_recover = open("player_dict.pickle", "rb")#New file opened for reading

    player_dict = pickle.load(pickle_recover)
    #score = player_dict[player_name_entry]
    score = player_dict.get(player_name_entry)

    #The below code is to catch the exception if KeyError(New Player not found in the dictionary) occured
    if score:
        score_label.config(text = "Score " + str(score), font = ("Arial", 20))
    else:
        print("Updating dictionary with new player name " + player_name_entry)
        score = 0
        player_dict[player_name_entry] = score #Since a new player is found(Not found in pickled file) the score entered is 0.
        score_label.config(text = "Score " + str(score), font = ("Arial", 20))#Updating the score on the screen for the new player


    start_button.config(text = "Started", font = ("Arial", 20))
    #Updating the leader_board label
    player_dict_str = str(player_dict)#Converting the dictionary to string for string manipulation
    player_dict_str = player_dict_str.replace("{", "")
    player_dict_str = player_dict_str.replace("}", "")
    player_dict_str = player_dict_str.replace(",", "\n")
    leader_label.config(text = "Leader Board\n" + player_dict_str, font = ("Arial", 15))

    if debug:
        print("From Start game_start : " + str(game_start))
        print("From Start Name : " + player_name + " " + "Score" + " " + str(score))

def stop():
    global game_start
    global player_name
    global score
    global player_dict
    game_start = 0
    #player_name_entry = ""
    start_button.config(text = "Restart", font = ("Arial", 20))

    #Adding elements or updating player_dict and pickle the data
    player_name_entry = player_entry.get()

    player_dict[player_name_entry] = score#Updating the entry of the present score for the player_name_entry
    #Pickling
    pickling_data = open("player_dict.pickle", "wb") #opening a pickling file called player_dict.pickle in write and binary mode
    pickle.dump(player_dict, pickling_data)
    pickling_data.close()

    if debug:
        print("From Stop game_start : " + str(game_start))
        print("Player Name: " + player_name_entry)
        print("Game Dictionary : ", player_dict)
        print("Testing pickle")
        pickle_recover = open("player_dict.pickle", "rb")
        player_dict = pickle.load(pickle_recover)
        print("From Stop player_dict : " + str(player_dict))
        print("From Stop player name from pickle dict : " + str(player_dict[player_name_entry]))

#Placing the score on the screen

score_label = Label(sky_canvas, text = "Score " + str(score), bg = "black", fg = "white", font = ("Arial", 20))
score_label.place(x = 1770, y = 100)

#Placing the start button
start_button = Button(sky_canvas, text = "Start", bg = "black", fg = "white", font = ("Arial", 20), command = start)
start_button.place(x= 1770, y = 150)

#Placing the stop button
stop_button = Button(sky_canvas, text = "Stop", bg = "black", fg = "white", font = ("Arial", 20), command = stop)
stop_button.place(x= 1770, y = 200)

#Leader Board Label
leader_label = Label(sky_canvas, text = "Leader Board", font = ("Arial", 15), bg = "black", fg = "white")
leader_label.place(x = 1770, y = 300)

#Player Name Entry Label
player_label = Label(sky_canvas, text = "Name", font = ("Arial", 20), bg = "black", fg = "white")
player_label.place(x = 1600, y = 750)

#Player name entry box
player_name = ""
player_entry = Entry(sky_canvas, textvariable = player_name, fg = "white", bg = "black", font = ("Arial", 20))
player_entry.place(x = 1600, y = 800)


#Making the space telescope move
sky_canvas.bind_all("<Right>", moveRight)
sky_canvas.bind_all("<Left>", moveLeft)
leader_label.bind("<Motion>", cheat_score)
sky_canvas.bind_all("<b>", boss_key)
sky_canvas.after(5000, appear)
sky_canvas.after(1000, vesta_appear)
sky_canvas.after(1000, pallas_appear)
sky_canvas.after(1000, start_screen_appear)

print("Before mainloop")
window.mainloop()
