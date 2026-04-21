import pygame

class jumppad:
    def __init__(self):
        self.jumppadframew = 64
        self.jumppadframeh = 64
        self.jumppadframecount = 2
        self.jumppadanimspeed = 0.1

        self.jumppad = pygame.image.load("gfx/jumppadspritesheet_idle.png").convert_alpha()

        self.jumppadframes = []
        for i in range(self.jumppadframecount):
            jumppadframe = self.jumppad.subsurface(pygame.Rect(i * self.jumppadframew, 0, self.jumppadframew, self.jumppadframeh))
            jumppadframe = pygame.transform.scale(jumppadframe, (64, 64))
            self.jumppadframes.append(jumppadframe)

    def jumppadcreate(self, jumppad, jumppadx, jumppady):
        jumppadimg = pygame.transform.scale(jumppad, (64, 64))
        jumppadrect = jumppadimg.get_rect(topleft=(jumppadx, jumppady))
        return (jumppadimg, jumppadrect)