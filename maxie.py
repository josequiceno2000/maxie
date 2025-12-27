class Maxie:
    def __init__(self, actor):
        self.actor = actor

    def set_position(self, x, y):
        self.actor.pos = (x, y)

    def set_opacity(self, opacity):
        self.actor.opacity = opacity

    def draw(self):
        self.actor.draw()