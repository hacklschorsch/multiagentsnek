import bhi160
import vibra
import display
from apps.multiagentsnek.agent import Agent


disp = display.open()
q = [] # queue
QLEN = 10 # enuff is enuff!


class Snek(Agent):

    sens = bhi160.BHI160Accelerometer()

    
    def move(self):
        def clamp(val):
            return -1.0 if val < -1.0 else 1.0 if val > 1.0 else val

        samples = self.sens.read()
        for s in samples:
            if len(q) == QLEN:
                q.pop(0)
            x = 160 - int((clamp(s.x) + 1.0) * 80)
            y = int((clamp(s.y) + 1.0) * 40)
            q.append((x, y))

    
    def paint(self):
        for i in range(0, len(q) - 1):
            c = int(20 + 235 * i / (len(q) - 1)) # color
            disp.line(q[i][0], q[i][1], q[i + 1][0], q[i + 1][1], col=(c,c,c), size=2)


    def collide(self):
        if len(q) < 4:
            return

        def lines_intersect(a,b,c,d, p,q,r,s):
            """ Thanks https://stackoverflow.com/a/24392281 """
            det = (c - a) * (s - q) - (r - p) * (d - b)
            if det == 0:
                return False
            else:
                llama = ((s - q) * (r - a) + (p - r) * (s - b)) / det
                gamma = ((b - d) * (r - a) + (c - a) * (s - b)) / det
                return (0 < llama and llama < 1) and (0 < gamma and gamma < 1)

        for i in range(0, len(q) - 3):
            if lines_intersect(q[i][0], q[i][1], q[i+1][0], q[i+1][1],
                               q[-2][0], q[-2][1], q[-1][0], q[-1][1]):
                # u hev eaten a rather large chunk of urself!!
                vibra.vibrate(160)
                global QLEN
                QLEN -= 10
                for i in range(10):
                    if len(q) >= 4:
                        q.pop(0)
                return

