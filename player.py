import pygame

playerframew = 32
playerframeh = 64
playerw = 64
playerh = 128
playerx = 200
playery = 200
playerframecount = 4
playerspeed = 5
playergravity = 1
playerjumpstrength = -18
playeranimspeed = 0.15

playersheet = pygame.image.load("gfx/playerspritesheet_walk_idle.png").convert_alpha()
playerjump = pygame.image.load("gfx/playerspritesheet_jump.png").convert_alpha()
playercrouch = pygame.image.load("gfx/playerspritesheet_crouch.png").convert_alpha()

playerframes = []
for i in range(playerframecount):
    playerframe = playersheet.subsurface(
        pygame.Rect(i * playerframew, 0, playerframew, playerframeh)
    )
    playerframe = pygame.transform.scale(playerframe, (playerw, playerh))
    playerframes.append(playerframe)
    
playercrouchframe = pygame.transform.scale(playercrouch, (playerw, playerh))
playerjumpframe = pygame.transform.scale(playerjump, (playerw, playerh))

player = playerframes[0]
playerrect = player.get_rect(topleft=(playerx, playery))
playervely = 0
playerframeindex = 0
playerright = True

playerspawnx = playerrect.x
playerspawny = playerrect.y

def playerreset():
    global playerrect, playervely, ground

    playerrect.x = playerspawnx
    playerrect.y = playerspawny

    playervely = 0

    ground = False