import pygame

def floorcreate(floor, floorx, floory, floorw, floorh):
    floorimg = pygame.transform.scale(floor, (floorw, floorh))
    floorrect = floorimg.get_rect(topleft=(floorx, floory))
    return (floorimg, floorrect)

def lanterncreate(lantern, lanternx, lanterny):
    lanternimg = pygame.transform.scale(lantern, (64, 64))
    lanternrect = lanternimg.get_rect(topleft=(lanternx, lanterny))
    return (lanternimg, lanternrect)

def finishcreate(finish, finishx, finishy):
    finishimg = pygame.transform.scale(finish, (64, 128))
    finishrect = finishimg.get_rect(topleft=(finishx, finishy))
    return (finishimg, finishrect)

def voidcreate(void, voidx, voidy, voidw, voidh):
    voidimg = pygame.transform.scale(void, (voidw, voidh))
    voidrect = voidimg.get_rect(topleft=(voidx, voidy))
    return (voidimg, voidrect)