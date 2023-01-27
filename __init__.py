import display
import utime
from apps.multiagentsnek.snek import Snek
from apps.multiagentsnek.cookie import Cookie
from apps.multiagentsnek.referee import Referee


disp = display.open()
agents = [Snek(), Cookie(), Referee()]


while True:
    utime.sleep(0.03) # 30 fps

    disp.clear()

    for agent in agents:
        agent.run()
    
    disp.update()

