import pygame

class coin:
    def __init__(self):
        self.coinframew = 64
        self.coinframeh = 64
        self.coinframecount = 6
        self.coinanimspeed = 0.15

        self.coin = pygame.image.load("gfx/coinspritesheet.png").convert_alpha()

        self.coinframes = []
        for i in range(self.coinframecount):
            coinframe = self.coin.subsurface(pygame.Rect(i * self.coinframew, 0, self.coinframew, self.coinframeh))
            coinframe = pygame.transform.scale(coinframe, (64, 64))
            self.coinframes.append(coinframe)

    def coincreate(self, coin, coinx, coiny):
        coinimg = pygame.transform.scale(coin, (64, 64))
        coinrect = coinimg.get_rect(topleft=(coinx, coiny))
        return (coinimg, coinrect)