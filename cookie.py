import urandom
import vibra
import display
from apps.multiagentsnek.agent import Agent
from apps.multiagentsnek import snek


disp = display.open()


class Cookie(Agent):

    def __init__(self):
        self.coords = (0,0) # looks like a face (0,0)
        self.respawn()


    def respawn(self):
        self.coords = (urandom.randint(10, 149), urandom.randint(10, 69))


    def collide(self):
        if len(snek.q) < 3:
            return

        if (abs(snek.q[-1][0] - self.coords[0]) <= 2 and
            abs(snek.q[-1][1] - self.coords[1]) <= 2):
            vibra.vibrate(20)
            snek.QLEN += 2 # who says uppercase variables need to be constant
            self.respawn()


    def paint(self):
        disp.circ(self.coords[0], self.coords[1], 2)

