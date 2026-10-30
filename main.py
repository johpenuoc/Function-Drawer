import pygame
import sys
from pygame.locals import *

from spiral import Spiral

class Main:
    def __init__(self):
        self.win = pygame.display.set_mode((1200, 900))

        self.clock = pygame.time.Clock()

        self.s = Spiral(self)
        self.dt = 0

    def run(self):
        while 1:
            self.dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEWHEEL:
                    msdir = event.y * -1
                    if msdir > 0:
                        self.s.scale += msdir * self.s.scale
                    else:
                        if self.s.scale <= 0.9:
                            self.s.scale = abs(self.s.scale) - (abs(self.s.scale) / 10)
                        else:
                            self.s.scale += msdir * (self.s.scale / 2)
                            if self.s.scale < 1:
                                self.s.scale = 0.9

            self.win.fill((0, 0, 0))

            self.s.draw(True)

            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.run()