import pygame
from pygame.locals import *
import sys
import math
import random

pygame.init()
# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (243, 236, 18)
#TokenFormat
TokenFormat = [
((25, 25), 50),
((5,25), (35, 25), 25),
((5,25), (30, 25), (25, 20), 20),
((5,25), (30, 25), (5,20), (30,20), 20),
((5,40), (30, 40), (5,15), (30,15), (25, 25), 20),
((5,40), (30, 40), (55, 40), (5,15), (30,15), (55,15), 20)]
#Representations of each character ((Starting/Current Level of Stat), (Template for increments)) (Stats ordered: Speed, Might, Sanity, Knowledge)
characters = {
"Madame": [(3, (7,6,6,5,5,3,3,2,-1)), (4, (6,5,5,5,4,3,3,2,-1)), (3, (8,8,7,6,5,4,4,4,-1)), (4, (6,6,5,4,4,4,3,1,-1))],
"Vivian": [(4, (8,7,6,4,4,4,4,3,-1)), (3, (6,6,5,4,4,2,2,2,-1)), (3, (8,8,7,6,5,4,4,4,-1)), (4, (7,6,6,5,5,5,5,4,-1))],
"Brandon": [(3, (8,7,6,5,4,4,4,3,-1)), (4, (7,6,6,5,4,3,3,2,-1)), (4, (8,7,6,5,4,3,3,3,-1)), (3, (7,6,6,5,5,3,3,1,-1))],
"Peter": [(4, (7,7,6,6,4,3,3,3,-1)), (3, (8,6,5,5,4,3,3,2,-1)), (4, (7,6,6,5,4,4,4,3,-1)), (3, (8,7,7,6,5,4,4,3,-1))],
"Missy": [(3, (7,7,6,6,6,5,4,3,-1)), (4, (7,6,5,4,3,3,3,2,-1)), (3, (7,6,5,5,4,3,2,1,-1)), (4, (6,6,6,5,4,4,3,2,-1))],
"Zoe": [(4, (8,8,6,5,4,4,4,4,-1)), (4, (7,6,4,4,3,3,2,2,-1)), (3, (8,7,6,6,5,5,4,3,-1)), (3, (5,5,5,4,4,3,2,1,-1))],
"Heather": [(3, (8,7,6,6,5,4,3,3,-1)), (3, (8,7,6,5,4,3,3,3,-1)), (3, (6,6,6,5,4,3,3,3,-1)), (5, (8,7,6,5,4,3,3,2,-1))],
"Jenny": [(4, (8,6,5,4,4,4,3,2,-1)), (3, (8,6,5,4,4,4,4,3,-1)), (5, (6,5,4,4,4,2,1,1,-1)), (3, (8,6,5,4,4,3,3,2,-1))],
"Darrin": [(5, (8,7,7,6,5,4,4,4,-1)), (3, (7,6,6,5,4,3,3,2,-1)), (3, (7,5,5,5,4,3,2,1,-1)), (3, (7,5,5,5,4,3,3,2,-1))],
"Ox": [(5, (6,5,5,4,3,2,2,2,-1)), (3, (8,8,7,6,6,5,5,4,-1)), (3, (7,6,5,5,4,3,2,2,-1)), (3, (6,6,5,5,3,3,2,2,-1))],
"Father": [(3, (7,7,6,5,4,3,3,2,-1)), (3, (7,5,5,4,4,2,2,1,-1)), (5, (8,7,7,6,5,5,4,3,-1)), (4, (8,6,6,5,4,3,3,1,-1))],
"Doctor": [(4, (6,6,5,5,4,4,2,2,-1)), (3, (6,6,5,5,4,3,2,1,-1)), (3, (7,6,5,5,4,3,3,1,-1)), (5, (8,7,6,5,5,5,5,4,-1))]
}

enlargebleSurfaces = [4]

tileBack = [None]

bg = pygame.image.load("Images/Backgrounds/BoardBG.png")
startMenubg = pygame.image.load("Images/Backgrounds/Menu.png")
#Blue Characters
madameStats = pygame.image.load("Images/PlayerStats/BlueMadame.png")
madameTok = pygame.image.load("Images/PlayerTokens/MadameTok.png")
vivianStats = pygame.image.load("Images/PlayerStats/BlueVivian.png")
vivianTok = pygame.image.load("Images/PlayerTokens/VivianTok.png")
#Green Characters
brandonStats = pygame.image.load("Images/PlayerStats/GreenBrandon.png")
brandonTok = pygame.image.load("Images/PlayerTokens/BrandonTok.png")
peterStats = pygame.image.load("Images/PlayerStats/GreenPeter.png")
peterTok = pygame.image.load("Images/PlayerTokens/PeterTok.png")
#Orange Characters
missyStats = pygame.image.load("Images/PlayerStats/OrangeMissy.png")
missyTok = pygame.image.load("Images/PlayerTokens/MissyTok.png")
zoeStats = pygame.image.load("Images/PlayerStats/OrangeZoe.png")
zoeTok = pygame.image.load("Images/PlayerTokens/ZoeTok.png")
#Purple Characters
heatherStats = pygame.image.load("Images/PlayerStats/PurpleHeather.png")
heatherTok = pygame.image.load("Images/PlayerTokens/HeatherTok.png")
jennyStats = pygame.image.load("Images/PlayerStats/PurpleJenny.png")
jennyTok = pygame.image.load("Images/PlayerTokens/JennyTok.png")
#Red Characters
darrinStats = pygame.image.load("Images/PlayerStats/RedDarrin.png")
darrinTok = pygame.image.load("Images/PlayerTokens/DarrinTok.png")
oxStats = pygame.image.load("Images/PlayerStats/RedOX.png")
oxTok = pygame.image.load("Images/PlayerTokens/OxTok.png")
#White Characters
fatherStats = pygame.image.load("Images/PlayerStats/WhiteFather.png")
fatherTok = pygame.image.load("Images/PlayerTokens/FatherTok.png")
professorStats = pygame.image.load("Images/PlayerStats/WhiteProfessor.png")
professorTok = pygame.image.load("Images/PlayerTokens/ProfessorTok.png")
#Card Backs
omenDeckBack = pygame.image.load("Images/TileBacks/OmenBack.jpg")
itemDeckBack = pygame.image.load("Images/TileBacks/ItemBack.jpg")
eventDeckBack = pygame.image.load("Images/TileBacks/EventBack.jpg")

#MapList
MapList = [[None for i in range(12)] for j in range(5)]
#Tiles
tilesimage = pygame.image.load("Images/FloorTiles/FloorTiles.jpg")
entraceimage = pygame.image.load("Images/FloorTiles/Entrance.jpg")
tiles = []
for i in range(0,4096,512):
    for j in range(0,4096,512):
        tempsurf = pygame.Surface((512,512))
        tempsurf.blit(tilesimage, (0,0), (j,i,512,512))
        tiles.append(tempsurf.copy())
for i in range(0,1536,512):
    tempsurf = pygame.Surface((512,512))
    tempsurf.blit(entraceimage, (0,0), (i,0,512,512))
    tiles.append(tempsurf.copy())
tempsurf = pygame.Surface((512,512), pygame.SRCALPHA, 32)
tempsurf.blit(entraceimage, (0,0), (1536,0,77,512))
tiles.append(tempsurf.copy())

#TileBacks
Groundimage = pygame.image.load("Images/TileBacks/Floors/Ground.jpg")
Upperimage = pygame.image.load("Images/TileBacks/Floors/Upper.jpg")
Roofimage = pygame.image.load("Images/TileBacks/Floors/Roof.jpg")
RUimage = pygame.image.load("Images/TileBacks/Floors/R&U.jpg")
RUBimage = pygame.image.load("Images/TileBacks/Floors/R&U&B.jpg")
RUGimage = pygame.image.load("Images/TileBacks/Floors/R&U&G.jpg")
UGimage = pygame.image.load("Images/TileBacks/Floors/U&G.jpg")
UBimage = pygame.image.load("Images/TileBacks/Floors/U&B.jpg")
GBimage = pygame.image.load("Images/TileBacks/Floors/G&B.jpg")
UGBimage = pygame.image.load("Images/TileBacks/Floors/U&G&B.jpg")
allFloorsimage = pygame.image.load("Images/TileBacks/Floors/AllFloors.jpg")
Basementimage = pygame.image.load("Images/TileBacks/Floors/Basement.jpg")
# Assign FPS a value
FPS = 60
FramePerSec = pygame.time.Clock()
#Representaions of players (Color: [Selection (-1 not selected, 0 = first choice, 1 = second choice), StatsTile Image, token Image, Stats Location, Hand Location, Player Location])
players = {
"Blue": [-1, None, None, (60,142), (0,0), (3,6)],
"Red": [-1, None, None, (60,682), (0,0), (3,6)],
"Orange": [-1, None, None, (480, 769), (0,0), (3,6)],
"White": [-1, None, None, (1184,769), (0,0), (3,6)],
"Purple": [-1, None, None, (1604,142), (0,0), (3,6)],
"Green": [-1, None, None, (1604,682), (0,0), (3,6)]
}

#Representations of card piles (Type: Left, Top, Width, Height, List) (Tiles have Tuple with 2nd Value
#(1 = Ground, 2 = Upper, 3 = Roof, 4 = R&U, 5 = R&U&B, 6 = R&U&G, 7 = U&G, 8 = U&B, 9 = G&B, 10 = U&G&B, 11 = All, 12 = Basement))
cardpiles = {
"Omens": (780, 70, 75, 144,
["Bite", "Bloodstone", "Book", "Box", "Cat", "Crystal Ball", "Dog", "Girl", "Holy Symbol", "Key", "Letter", "Madman", "Mask", "Medallion", "Photograph", "Ring", "Rope", "Skull", "Spear", "Spirit Board", "Vial"]),
"OmenDis": (875, 70, 75, 144, []),
"Items": (970, 70, 75, 144,
["Adrenaline", "Amulet", "Feather", "Armor", "Axe", "Bell", "Blood Dagger", "Blueprint", "Boomstick", "Bottle", "Camcorder", "Candle", "Robe", "Chainsaw", "Chalk", "Dice", "Device", "Dynamite",
"Effigy", "Salve", "Idol", "Locket", "Lucky Stone", "MedKit", "Music Box", "Gloves", "Puzzle", "Rabbit", "Revolver", "Sacrifical Dagger", "Salts", "Snake Oil", "Teapot"]),
"ItemDis": (1065, 70, 75, 144, []),
"Event": (1160, 70, 75, 144,
["Mom Hope", "Acupuncture", "Angry Being", "Bloody Vision", "Burial", "Burning Man", "Closet Door", "Contract", "Creepy Crawlies", "Creepy Puppet", "Debris", 'Sounds', 'Drip', 'Flytrap', 'FootSteps',
'Funeral', 'Machine', 'Grave', 'Groundskeeper', 'Hanged Men', 'Shiek', 'Image 1', 'Image 2', 'Meant to Be', "Jonah's Turn", 'Lightning', 'Lights Out', 'Safe', 'Misty Arch', 'Mist From Walls', 'Mutant', 'Slide',
'Night View', 'Phone Call', 'Possession', 'Revolving Wall', 'Rotten', "Secret Passage", 'Secret Stairs', 'Shrieking Wind', "Silence", 'Skeletons', 'Smoke', "Something Hidden", 'Something Slimy', 'Spider',
'Beckoning', 'Left Hand', 'Lost One', 'Voice', 'The Walls', 'Have Eyes', 'Webs', 'What The', 'What Year', 'Whoops']),
"Eventdis": (1255, 70, 75, 144, []),
"Tiles": (540, 70, 100, 100,
[('Panic Room', 11, 3), ('Creaky', 10, 4), ('Dusty', 10, 5), ('Game Room', 10, 6), ('Junk Room', 10, 7), ('Mystic Elevator', 10, 8), ('Organ Room', 10, 9), ("Statutary", 10, 10), ('Spiral Staircase', 6, 11),
('Study', 6, 12), ('Locked Room', 5, 13), ('Drawing Room', 4, 14), ('Nursery', 4, 15), ('Sewing Room', 4, 16), ('Solarium', 4, 17), ('Widows Walk', 4, 18), ('Rookery', 3, 19), ('Gymnasium', 8, 20),
('Operating', 8, 21), ('Research', 8, 22), ('Servants', 8, 23), ('Storeroom', 8, 24), ('Vault', 8, 25), ('Attic', 2, 26), ('Balcony', 2, 27), ("Bedroom", 2, 28), ('Gallery', 2, 29), ('Master Bedroom', 2, 30),
('Tower', 2, 31), ('Bathroom', 7, 32), ('Bloody Room', 7, 33), ('Chapel', 7, 34),
('Charred Room', 7, 35), ('Collapsed Room', 7, 36), ('Conservatory', 7, 37), ('Library', 7, 38), ('Theater', 7, 39), ('Ballroom', 1, 40), ('Coal Chute', 1, 41), ('Dining Room', 1, 42),
('Gardens', 1, 43), ('Graveyard', 1, 44), ('Patio', 1, 45), ('Tree House', 1, 46), ('Abandoned Room', 9, 47), ('Arsenal', 9, 48), ('Kitchen', 9, 49), ('Laundry', 9, 50), ('Menagerie', 9, 51),
('Catacombs', 12, 52), ('Cave', 12, 53), ('Chasm', 12, 54), ('Crypt', 12, 55), ('Dungeon', 12, 56), ('Furnace', 12, 57),
('Larder', 12, 58), ('Pentagram', 12, 59), ('Stairs from Basement', 12, 60), ('Storm Cellar', 12, 61), ('Underground Lake', 12, 62), ('Wine Cellar', 12, 63)]),
"TileDis": (660, 70, 100, 100, [])
}
boardtiles = [ ]

DISPLAYSURF = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Betrayal at House on the Hill")
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


def rectbutton(abutton):
    mouse = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if((x >= abutton[0] and x <= abutton[0] + abutton[2]) and (y >= abutton[1] and y <= abutton[1] + abutton[3])):
        pygame.draw.rect(DISPLAYSURF, YELLOW, (abutton[0], abutton[1], abutton[2], abutton[3]), 3)
        pygame.display.update()
        if mouse[0]:
            return True
    else:
        pygame.draw.rect(DISPLAYSURF, BLACK, (abutton[0], abutton[1], abutton[2], abutton[3]), 3)
        pygame.display.update()
        return False

def start():
    DISPLAYSURF.blit(startMenubg, (0,0))
    #Buttons represented (Name: (left, top, width, height))
    menubuttons = {
    "Start": (1000, 410, 500, 100),
    "Quit": (1000, 520, 500, 100)
    }
    buttons = []
    for button in menubuttons:
        thetext = button
        location = menubuttons[thetext]
        font = pygame.font.Font('freesansbold.ttf',120)
        text = font.render(thetext, True, BLACK)
        textRect = text.get_rect()
        textRect.top = location[1] - 2
        textRect.height = location[3]
        textRect.left = location[0] + (location[2] - textRect.width) / 2
        pygame.draw.rect(DISPLAYSURF, WHITE, (location[0], location[1], location[2], location[3]))
        pygame.draw.rect(DISPLAYSURF, BLACK, (location[0], location[1], location[2], location[3]), 3)
        buttons.append((text, textRect))
    for i in buttons:
        DISPLAYSURF.blit(i[0], i[1])
        pygame.display.update()
    while True:
        if rectbutton(menubuttons['Start']):
            return
        elif rectbutton(menubuttons['Quit']):
            pygame.quit()
            sys.exit()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

def selectCard(selection):
    pass

#(1 = Ground, 2 = Upper, 3 = Roof, 4 = R&U, 5 = R&U&B, 6 = R&U&G, 7 = U&G, 8 = U&B, 9 = G&B, 10 = U&G&B, 11 = All, 12 = Basement))
def getTileBack(num):
    if(num == 1):
        image = Groundimage
    if(num == 2):
        image = Upperimage
    if(num == 3):
        image = Roofimage
    if(num == 4):
        image = RUimage
    if(num == 5):
        image = RUBimage
    if(num == 6):
        image = RUGimage
    if(num == 7):
        image = UGimage
    if(num == 8):
        image = UBimage
    if(num == 9):
        image = GBimage
    if(num == 10):
        image = UGBimage
    if(num == 11):
        image = allFloorsimage
    if(num == 12):
        image = Basementimage
    tileBack[0] = image

def shuffleDeck(deck):
    random.seed()
    decklist = cardpiles[deck][4]
    newlist = []
    while(len(decklist) > 0):
        if(len(decklist) == 1):
            newlist.append(decklist.pop(0))
        else:
            newlist.append(decklist.pop(random.randrange(len(decklist) - 1)))
    cardpiles[deck] = (cardpiles[deck][0], cardpiles[deck][1], cardpiles[deck][2], cardpiles[deck][3], newlist)
def checkZoomin():
    x, y = pygame.mouse.get_pos()
    if(pygame.key.get_pressed()[pygame.K_LALT]):
            for surface in enlargebleSurfaces[1:]:
                if((x >= surface[1] and x <= surface[1] + surface[3]) and (y >= surface[2] and y <= surface[2] + surface[4])):
                    enlarge(surface[0], surface[3], surface[4])
                    break

def enlarge(surface, width, height):
    zoomedIn = pygame.transform.scale(surface, (int(width * enlargebleSurfaces[0]), int(height * enlargebleSurfaces[0])))
    DISPLAYSURF.blit(zoomedIn, (int(960 - width * enlargebleSurfaces[0]/2), int(540 -  height * enlargebleSurfaces[0]/2)))
    pygame.display.update()
    for i in range(0,1000):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 5 and enlargebleSurfaces[0] > 1.6:
                    enlargebleSurfaces[0] -= 0.5
                elif event.button == 4 and enlargebleSurfaces[0] < 8:
                    enlargebleSurfaces[0] += 0.5

def numPlayerSelection():
    circleCenter = (660,534)
    sliding = False
    numPlayers = 3
    enterbutton = (710, 632, 500, 100)
    pygame.draw.rect(DISPLAYSURF, BLACK, enterbutton, 3)
    while True:
        DISPLAYSURF.blit(bg, (0,0))

        font = pygame.font.Font('freesansbold.ttf',120)
        entertext = font.render('Enter', True, BLACK)
        entertextRect = entertext.get_rect()
        entertextRect.top = enterbutton[1] - 2
        entertextRect.height = enterbutton[3]
        entertextRect.left = enterbutton[0] + (enterbutton[2] - entertextRect.width) / 2
        DISPLAYSURF.blit(entertext, entertextRect)

        font = pygame.font.Font('freesansbold.ttf', 80)
        playertext = font.render('How Many Players?', True, BLUE)
        playersRect = playertext.get_rect()
        playersRect.left = (1920 - playersRect.width) / 2
        playersRect.top = 300
        DISPLAYSURF.blit(playertext, playersRect)

        numtext = font.render(str(numPlayers), True, BLACK)
        numRect = numtext.get_rect()
        numRect.left = (1920 - numRect.width) / 2
        numRect.top = 400
        DISPLAYSURF.blit(numtext, numRect)

        pygame.draw.rect(DISPLAYSURF, BLACK, (660,532,600,4))
        pygame.draw.rect(DISPLAYSURF, BLACK, (858,522,4,24))
        pygame.draw.rect(DISPLAYSURF, BLACK, (1058,522,4,24))
        pygame.draw.circle(DISPLAYSURF, BLACK, circleCenter, 10)

        mouse = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        distance = (abs(x - circleCenter[0])**2 + abs(y - circleCenter[1])**2)**(0.5)
        if (mouse[0] and (distance <= 10)):
            sliding = True
        elif(not mouse[0]):
            sliding = False
        if(sliding and x - circleCenter[0]  >= 200 and circleCenter[0] != 1260):
            circleCenter = (circleCenter[0] + 200, 534)
            numPlayers += 1
        elif(sliding and x - circleCenter[0]  <= -200 and circleCenter[0] != 660):
            circleCenter = (circleCenter[0] - 200, 534)
            numPlayers -= 1
        pygame.display.update()
        if rectbutton(enterbutton):
            break
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    return numPlayers

def playerSelection(numPlayers):
    font = pygame.font.Font('freesansbold.ttf',120)
    nodes = [(295,673),(1635,673),(295,407),(1635,407),(571,673),(1369,673),(837,673),(1103,673),(571,407),(1369,407),(837,407),(1103,407)]
    possibleSelections = [(madameStats, vivianStats), (brandonStats, peterStats), (missyStats, zoeStats), (heatherStats, jennyStats), (darrinStats, oxStats), (fatherStats, professorStats)]
    players = []
    mouse = pygame.mouse.get_pressed()
    length = 12
    for i in range(numPlayers):
        mousedown = True
        while mousedown:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    mousedown = False
        DISPLAYSURF.blit(bg, (0,0))
        playertext = font.render('Player ' + str(i+1) + " select a character", True, GREEN)
        playerRect = playertext.get_rect()
        playerRect.top = 100
        playerRect.left = (1920 - playerRect.width)/2
        DISPLAYSURF.blit(playertext, playerRect)
        for j in range(length):
            playerOption = pygame.transform.scale(possibleSelections[int(j/2)][j % 2], (256,256))
            DISPLAYSURF.blit(playerOption, (nodes[j][0] - 128, nodes[j][1] - 128))
            pygame.display.update()
        broken = False
        while not broken:
            for k in range(length):
                if rectbutton((nodes[k][0] - 128, nodes[k][1] - 128, 256, 256)):
                    if(j % 2 == 0):
                        players.append(possibleSelections[int(k/2)][0])
                    else:
                        players.append(possibleSelections[int(k/2)][1])
                    possibleSelections.pop(int(k/2))
                    nodes.pop(0)
                    nodes.pop(0)
                    broken = True
                    length = length - 2
                    break
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
    return players

def genPlayers(statsTiles):
    try:
        statsTiles[statsTiles.index(madameStats)] = characters["Madame"]
        players["Blue"][0] = 0
        players["Blue"][1] = pygame.transform.rotate(madameStats, -90)
        players["Blue"][2] = madameTok
        enlargebleSurfaces.append((madameStats, players["Blue"][3][0], players["Blue"][3][1], 256, 256))
    except:
        pass
    try:
        statsTiles[statsTiles.index(vivianStats)] = characters["Vivian"]
        players["Blue"][0] = 1
        players["Blue"][1] = pygame.transform.rotate(vivianStats, -90)
        players["Blue"][2] = vivianTok
        enlargebleSurfaces.append((vivianStats, players["Blue"][3][0], players["Blue"][3][1], 256, 256))
    except:
        pass
    try:
        statsTiles[statsTiles.index(brandonStats)] = characters["Brandon"]
        players["Green"][0] = 0
        players["Green"][1] = pygame.transform.rotate(brandonStats, 90)
        players["Green"][2] = brandonTok
        enlargebleSurfaces.append((brandonStats, players["Green"][3][0], players["Green"][3][1], 256, 256))
    except:
        pass
    try:
        statsTiles[statsTiles.index(peterStats)] = characters["Peter"]
        players["Green"][0] = 1
        players["Green"][1] = pygame.transform.rotate(peterStats, 90)
        players["Green"][2] = peterTok
        enlargebleSurfaces.append((peterStats, players["Green"][3][0], players["Green"][3][1], 256, 256))
    except:
        pass
    try:
        statsTiles[statsTiles.index(missyStats)] = characters["Missy"]
        players["Orange"][0] = 0
        players["Orange"][1] = missyStats
        players["Orange"][2] = missyTok
        enlargebleSurfaces.append((missyStats, players["Orange"][3][0], players["Orange"][3][1], 256, 256))
    except:
        pass
    try:
        statsTiles[statsTiles.index(zoeStats)] = characters["Zoe"]
        players["Orange"][0] = 1
        players["Orange"][1] = zoeStats
        players["Orange"][2] = zoeTok
        enlargebleSurfaces.append((zoeStats, players["Orange"][3][0], players["Orange"][3][1], 256, 256))
    except:
        pass
    try:
        statsTiles[statsTiles.index(heatherStats)] = characters["Heather"]
        players["Purple"][0] = 0
        players["Purple"][1] = pygame.transform.rotate(heatherStats, 90)
        players["Purple"][2] = heatherTok
        enlargebleSurfaces.append((heatherStats, players["Purple"][3][0], players["Purple"][3][1], 256, 256))
    except:
        pass
    try:
        statsTiles[statsTiles.index(jennyStats)] = characters["Jenny"]
        players["Purple"][0] = 1
        players["Purple"][1] = pygame.transform.rotate(jennyStats, 90)
        players["Purple"][2] = jennyTok
        enlargebleSurfaces.append((jennyStats, players["Purple"][3][0], players["Purple"][3][1], 256, 256))
    except:
        pass
    try:
        statsTiles[statsTiles.index(darrinStats)] = characters["Darrin"]
        players["Red"][0] = 0
        players["Red"][1] = pygame.transform.rotate(darrinStats, -90)
        players["Red"][2] = darrinTok
        enlargebleSurfaces.append((darrinStats, players["Red"][3][0], players["Red"][3][1], 256, 256))
    except:
        pass
    try:
        statsTiles[statsTiles.index(oxStats)] = characters["Ox"]
        players["Red"][0] = 1
        players["Red"][1] = pygame.transform.rotate(oxStats, -90)
        players["Red"][2] =oxTok
        enlargebleSurfaces.append((oxStats, players["Red"][3][0], players["Red"][3][1], 256, 256))
    except:
        pass
    try:
        statsTiles[statsTiles.index(professorStats)] = characters["Doctor"]
        players["White"][0] = 0
        players["White"][1] = professorStats
        players["White"][2] = professorTok
        enlargebleSurfaces.append((professorStats, players["White"][3][0], players["White"][3][1], 256, 256))
    except:
        pass
    try:
        statsTiles[statsTiles.index(fatherStats)] = characters["Father"]
        players["White"][0] = 1
        players["White"][1] = fatherStats
        players["White"][2] = fatherTok
        enlargebleSurfaces.append((fatherStats, players["White"][3][0], players["White"][3][1], 256, 256))
    except:
        pass
    return statsTiles

def setUpLandings():
    MapList[1][2] = ('Roof Landing', 2, 0)
    MapList[3][2] = ('Upper Landing', 1, 1)
    MapList[2][9] = ('Basement Landing', -1, 2)
    MapList[2][4] = ('Grand Staircase', 0, 64)
    MapList[2][5] = ('Foyer', 0, 65)
    MapList[2][6] = ('Entrance Hall', 0, 66)
    i = 0
    for row in MapList:
        j = 0
        for tile in row:
            if tile:
                DISPLAYSURF.blit(pygame.transform.scale(tiles[tile[2]], (100,100)), (358 + j * 100, 246 + i * 100))
                enlargebleSurfaces.append((tiles[tile[2]], 358 + j * 100, 246 + i * 100, 100, 100))
            j += 1
        i += 1
    MapList[2][7] = ('Outside', 0, 67)
    DISPLAYSURF.blit(pygame.transform.scale(tiles[67], (100,100)), (358 + 7 * 100, 246 + 2 * 100))

def showPlayerToks():
    # (358, 246) is starting corner
    # playerlocs = {}
    # for player in players:
    #     if not(players[player][5] in playerlocs):
    #         playerlocs[players[player][5]] = 1
    #     else:
    #         playerlocs[players[player][5]] += 1
    # for tile in playerlocs:
    #     numtoks = playerlocs[tile]
    #     template = TokenFormat[numtoks]
    #     for player in players:
    #         if tile == players[player][5]:
                pass

def setUpDecks():
    #Shuffle Decks
    for key in cardpiles:
        shuffleDeck(key)
    #Gen Tile Backs
    getTileBack(cardpiles["Tiles"][4][0][1])
    tileDeckBack = pygame.transform.scale(tileBack[0], (cardpiles["Tiles"][2], cardpiles["Tiles"][3]))
    DISPLAYSURF.blit(tileDeckBack, (cardpiles["Tiles"][0], cardpiles["Tiles"][1]))
    enlargebleSurfaces.append((tileBack[0], cardpiles["Tiles"][0], cardpiles["Tiles"][1], cardpiles["Tiles"][2], cardpiles["Tiles"][3]))
    #Draw Omen Back
    theomenDeckBack = pygame.transform.scale(omenDeckBack, (cardpiles["Omens"][2], cardpiles["Omens"][3]))
    DISPLAYSURF.blit(theomenDeckBack, (cardpiles["Omens"][0], cardpiles["Omens"][1]))
    enlargebleSurfaces.append((omenDeckBack, cardpiles["Omens"][0], cardpiles["Omens"][1], cardpiles["Omens"][2], cardpiles["Omens"][3]))
    #Draw Item Back
    theitemDeckBack = pygame.transform.scale(itemDeckBack, (cardpiles["Items"][2], cardpiles["Items"][3]))
    DISPLAYSURF.blit(theitemDeckBack, (cardpiles["Items"][0], cardpiles["Items"][1]))
    enlargebleSurfaces.append((itemDeckBack, cardpiles["Items"][0], cardpiles["Items"][1], cardpiles["Items"][2], cardpiles["Items"][3]))
    #Draw Event Back
    theeventDeckBack = pygame.transform.scale(eventDeckBack, (cardpiles["Event"][2], cardpiles["Event"][3]))
    DISPLAYSURF.blit(theeventDeckBack, (cardpiles["Event"][0], cardpiles["Event"][1]))
    enlargebleSurfaces.append((eventDeckBack, cardpiles["Event"][0], cardpiles["Event"][1], cardpiles["Event"][2], cardpiles["Event"][3]))
    #Draw Discards
    for key in cardpiles:
        if(len(cardpiles[key][4]) == 0):
            pygame.draw.rect(DISPLAYSURF, BLACK, (cardpiles[key][0], cardpiles[key][1], cardpiles[key][2], cardpiles[key][3]), 3)
    for player in players.values():
        playerStatsTile = pygame.transform.scale(player[1], (256,256))
        DISPLAYSURF.blit(playerStatsTile, player[3])

def genStart():
    CharacterStatsTiles = playerSelection(numPlayerSelection())
    characterStats = genPlayers(CharacterStatsTiles)
    playerList = list(players.keys())
    for i in range(len(playerList)):
        if(players[playerList[i]][0] != -1):
            pass
        else:
            del players[playerList[i]]
    DISPLAYSURF.blit(bg, (0,0))
    for i in range(358,1558,100):
        for j in range(246,746,100):
            pygame.draw.rect(DISPLAYSURF, BLACK, (i,j,100,100), 3)
    setUpDecks()
    setUpLandings()
    showPlayerToks()
    background = DISPLAYSURF.copy()
    while(True):
        DISPLAYSURF.blit(background, (0,0))
        checkZoomin()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

start()
genStart()
