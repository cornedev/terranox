import pygame

class windcharge:
    def __init__(self):
        self.windchargew = 64
        self.windchargeh = 64

        self.windcharge = pygame.image.load("gfx/itemwindcharge.png").convert_alpha()
    
    def windchargecreate(self, windchargex, windchargey):
        windchargeimg = pygame.transform.scale(self.windcharge, (64, 64))
        windchargerect = windchargeimg.get_rect(topleft=(windchargex, windchargey))
        return (windchargeimg, windchargerect)