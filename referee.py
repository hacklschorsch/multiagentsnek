import sys
import utime
import display
import leds
import color
from apps.multiagentsnek.agent import Agent
from apps.multiagentsnek import snek


disp = display.open()


class Referee(Agent):
    """ Shows sneks length """


    def move(self):
        if snek.QLEN <= 2:
            leds.set_all([color.RED for x in range(14)])
            utime.sleep(2)
            sys.exit("sneks ded bebe, sneks ded")


    def paint(self):
        disp.print(str(snek.QLEN), posx=120, posy=5)

