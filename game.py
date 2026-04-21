# - terranox, created by Corne, Steven, Jesse & Hans.
# - every single line of code is licensed under the MIT license.
# - copyright, the terranox team: 2025-2026.

import pygame
import sys

pygame.init()
pygame.mixer.init()
gamew = 1000
gameh = 700

gamescreen = pygame.display.set_mode((gamew, gameh))
gameicon = pygame.image.load("gfx/terranox.png").convert_alpha()
pygame.display.set_icon(gameicon)
pygame.display.set_caption("terranox")
gameclock = pygame.time.Clock()
gamefps = 60
gamefont = pygame.font.Font(None, 40)

from obstacles import *
from player import *
from audio import *
from enemies import *

from items.items import items
item = items()

musicstart()

camerax = 0
cameray = 0

worldw = 4000
worldh = 2000

floorsand = pygame.image.load("gfx/floorsand.png").convert_alpha()
floorsandstone = pygame.image.load("gfx/floorsandstone.png").convert_alpha()
floorsandblock = pygame.image.load("gfx/floorsandblock.png").convert_alpha()
floors = [
    #floor 1
    floorcreate(floorsand, 0, 636, 640, 64),
    floorcreate(floorsandstone, 0, 572, 640, 64),
    floorcreate(floorsandblock, 576, 508, 64, 64),
    #floor 2
    floorcreate(floorsand, 832, 636, 640, 64),
    floorcreate(floorsandstone, 832, 572, 640, 64),
    floorcreate(floorsandblock, 832, 508, 64, 64),
    floorcreate(floorsandblock, 1408, 508, 64, 64),
    #floor 3
    floorcreate(floorsandstone, 1664, 444, 640, 64),
    floorcreate(floorsandblock, 1600, 444, 64, 64),
    #floor 3 stairs
    floorcreate(floorsandblock, 1920, 380, 64, 64),
    floorcreate(floorsandblock, 1984, 316, 64, 64),
    floorcreate(floorsandblock, 2048, 252, 64, 64),
    floorcreate(floorsandblock, 2112, 188, 64, 64),
    floorcreate(floorsandblock, 2176, 188, 64, 64),
    floorcreate(floorsandblock, 2240, 188, 64, 64),
    floorcreate(floorsandblock, 2304, 636, 64, 64),
    #floor 4
    floorcreate(floorsandstone, 2688, 380, 640, 64),
]

lantern = pygame.image.load("gfx/lantern.png").convert_alpha()
lanterns = [
    lanterncreate(lantern, 100, 100),
]

finish = pygame.image.load("gfx/finish.png").convert_alpha()
finishes = [
    finishcreate(finish, 2128, 256),
]

void = pygame.image.load("gfx/void.png").convert_alpha()
voids = [
    voidcreate(void, 0, 1212, 10000, 64)
]

spikes = pygame.image.load("gfx/spikes.png").convert_alpha()
spikes = [
    #spikescreate(spikes, 1216, 508),
]

windcharges = [
    item.windchargecreate(0, 508),
]

jumppads = [
    {"rect": item.jumppadcreate(item.jumppadframes[0], 2304, 572)[1], "jumppadframeindex": 0}
]

def levelreset():
    global coins, goombas, coinscore, playerlives
    playerreset()

    coins = [
        {"rect": item.coincreate(item.coinframes[0], 300, 300)[1], "coinframeindex": 0},
        {"rect": item.coincreate(item.coinframes[0], 400, 300)[1], "coinframeindex": 0},
        {"rect": item.coincreate(item.coinframes[0], 500, 300)[1], "coinframeindex": 0},
        {"rect": item.coincreate(item.coinframes[0], 600, 300)[1], "coinframeindex": 0},
    ]
    coinscore = 0

    goombas = [
        {"rect": goombacreate(goombaframes[0], 1000, 100), "goombaframeindex": 0, "goombaalive": True, "goombakilledtimer": 15},
    ]

levelreset()

white = (255, 255, 255)
blue = (135, 206, 235)

ground = True
gamerunning = True
gamepaused = False
windchargehenk = True

gamepausetimer = 0
coinscore = 0
playerlives = 3
while gamerunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                if musicrunning:
                    pygame.mixer.music.pause()
                    musicrunning = False
                else:
                    pygame.mixer.music.unpause()
                    musicrunning = True
   
    if gamepaused:
        gamepausetimer -= 1
        pygame.display.flip()
        gameclock.tick(gamefps)
        if gamepausetimer <= 0:
            gamepaused = False
        continue

    gamedx = 0
    gameinput = pygame.key.get_pressed()
    if gameinput[pygame.K_a]:
        playerright = False
    if gameinput[pygame.K_d]:
        playerright = True
    if gameinput[pygame.K_LSHIFT]:
        playerspeed = 10
    if not gameinput[pygame.K_LSHIFT]:
        playerspeed = 5

    if not (gameinput[pygame.K_s] and ground):
        if gameinput[pygame.K_a]:
            gamedx = -playerspeed
        if gameinput[pygame.K_d]:
            gamedx = playerspeed
    playerrect.x += gamedx
    
    if not ground:
        player = playerjumpframe
        if not playerright:
            player = pygame.transform.flip(player, True, False)
    elif gameinput[pygame.K_s] and ground:
        player = playercrouchframe
        if not playerright:
            player = pygame.transform.flip(player, True, False)
    elif gamedx != 0:
        playerframeindex += playeranimspeed
        if playerframeindex >= len(playerframes):
            playerframeindex = 0
        player = playerframes[int(playerframeindex)]
        if not playerright:
            player = pygame.transform.flip(player, True, False)
    else:
        playerframeindex = 0
        player = playerframes[0]
        if not playerright:
            player = pygame.transform.flip(player, True, False)

    for floorimg, floorrect in floors:
        if playerrect.colliderect(floorrect):
            if gamedx > 0:
                playerrect.right = floorrect.left
            if gamedx < 0:
                playerrect.left = floorrect.right
    if gameinput[pygame.K_SPACE] and ground:
        playervely = playerjumpstrength
        ground = False
        playerjumpsfx()

    playervely += playergravity
    playerrect.y += playervely
    ground = False
    for floorimg, floorrect in floors:
        if playerrect.colliderect(floorrect):
            if playervely > 0:
                playerrect.bottom = floorrect.top
                playervely = 0
                ground = True
            elif playervely < 0:
                playerrect.top = floorrect.bottom
                playervely = 0

    camerax = playerrect.centerx - gamew // 2
    camerax = max(0, min(camerax, worldw - gamew))

    gamescreen.fill(blue)

    if windchargehenk == True:
        for item.windchargeimg, item.windchargerect in windcharges:
            gamescreen.blit(item.windchargeimg, (item.windchargerect.x -camerax, item.windchargerect.y - cameray))

    for jumppad in jumppads:
        jumppad["jumppadframeindex"] += item.jumppadanimspeed
        if jumppad["jumppadframeindex"] >= len(item.jumppadframes):
            jumppad["jumppadframeindex"] = 0

        jumppadcurrentframe = item.jumppadframes[int(jumppad["jumppadframeindex"])]
        gamescreen.blit(jumppadcurrentframe, (jumppad["rect"].x - camerax, jumppad["rect"].y - cameray))
    
    gamescreen.blit(player, (playerrect.x - camerax, playerrect.y - cameray))

    gamecoincounter = gamefont.render(f"coins: {coinscore}", True, white)
    gamescreen.blit(gamecoincounter, (20, 20))

    playerlivescounter = gamefont.render(f"lives: {playerlives}", True, white)
    gamescreen.blit(playerlivescounter, (20, 50))

    if playerlives == 0:
        pygame.quit()
        sys.exit()

    coinsnew = []
    for coin in coins:
        if playerrect.colliderect(coin["rect"]):
            coinscore += 1
            playercoinsfx() 
        else:
            coinsnew.append(coin)
    coins = coinsnew

    for coin in coins:
        coin["coinframeindex"] += item.coinanimspeed
        if coin["coinframeindex"] >= len(item.coinframes):
            coin["coinframeindex"] = 0

        coincurrentframe = item.coinframes[int(coin["coinframeindex"])]
        gamescreen.blit(coincurrentframe, (coin["rect"].x - camerax, coin["rect"].y - cameray))

    for finishimg, finishrect in finishes:
        gamescreen.blit(finishimg, (finishrect.x - camerax, finishrect.y - cameray))

    for floorimg, floorrect in floors:
        gamescreen.blit(floorimg, (floorrect.x - camerax, floorrect.y - cameray))

    for lanternimg, lanternrect in lanterns:
        gamescreen.blit(lanternimg, (lanternrect.x - camerax, lanternrect.y - cameray))

    for spikeimg, spikerect in spikes:
        gamescreen.blit(spikeimg, (spikerect.x -camerax, spikerect.y - cameray))

    goombasalive = []
    for goomba in goombas:
        if goomba["goombaalive"]:
            goombaupdate(goomba["rect"], floors)

        if playerrect.colliderect(goomba["rect"]["goombarect"]):
            if playervely > 0 and (playerrect.bottom - goomba["rect"]["goombarect"].top) < 20:
                playervely = -15
                goombakilledsfx()
                goomba["goombaalive"] = False
                goomba["goombakilledtimer"] = 15
            elif goomba["goombaalive"]:
                playerlives -= 1
                gamepaused = True
                gamepausetimer = 60
                playerreset()

        if goomba["goombaalive"]:
            goomba["goombaframeindex"] += goombaanimspeed
            if goomba["goombaframeindex"] >= len(goombaframes):
                goomba["goombaframeindex"] = 0
            goombacurrentframe = goombaframes[int(goomba["goombaframeindex"])]
        else:
            goombacurrentframe = goombakilled
            goomba["goombakilledtimer"] -= 1
            if goomba["goombakilledtimer"] <= 0:
                continue

        gamescreen.blit(goombacurrentframe, (goomba["rect"]["goombarect"].x - camerax, goomba["rect"]["goombarect"].y - cameray))
        goombasalive.append(goomba)

    goombas = goombasalive

    for finishimg, finishrect in finishes:
        if playerrect.colliderect(finishrect):
            playerlives = 3
            levelreset()

    for voidimg, voidrect in voids:
        if playerrect.colliderect(voidrect):
            playerlives -= 1
            levelreset()

    for spikeimg, spikerect in spikes:
        if playerrect.colliderect(spikerect):
            playerlives -= 1
            levelreset()

    for windchargeimg, windchargerect in windcharges:
        if gameinput[pygame.K_e] and playerrect.colliderect(windchargerect):
            playervely = -30
            windchargehenk = False

    for jumppad in jumppads:
        jumppadrect = jumppad["rect"]
        if playerrect.colliderect(jumppadrect):
            if playervely > 0 and playerrect.bottom - playervely <= jumppadrect.top:
                playerrect.bottom = jumppadrect.top
                playervely = -40
    
    pygame.display.flip()
    gameclock.tick(gamefps)

pygame.quit()
sys.exit()
