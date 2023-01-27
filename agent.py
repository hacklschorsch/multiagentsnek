class Agent:
    """ Abstract base class for all entities in our ``simulation''.
        Implement move(), collide() and paint() as you please.  """

    def move(self):
        """ Calculate new coordinates """
        pass

    def collide(self):
        """ Collision detection """
        pass

    def paint(self):
        """ Render """
        pass

    def run(self):
        """ Hello instruction pointer """
        self.move()
        self.collide()
        self.paint()

