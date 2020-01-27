from constants import display


class Bat:
    def __init__(self, size, velocity, pos_x):
        self.size = size
        self.velocity = velocity
        self.pos = [pos_x, (display.HEIGHT - size[1]) / 2]

    def get_rect(self):
        rectangle = [self.pos[0], self.pos[1], self.size[0], self.size[1]]

        return rectangle

    def move(self, direction):
        if (direction == "UP") and (self.pos[1] > 0):
            self.pos[1] -= self.velocity
        if (direction == "DOWN") and ((self.pos[1] + self.size[1]) < display.HEIGHT):
            self.pos[1] += self.velocity
