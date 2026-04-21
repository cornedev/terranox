import pygame

#class imports
from .coin import coin
from .windcharge import windcharge
from .jumppad import jumppad

class items(coin, windcharge, jumppad):
    def __init__(self):
        coin.__init__(self)
        windcharge.__init__(self)
        jumppad.__init__(self)