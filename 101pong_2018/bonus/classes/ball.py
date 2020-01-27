from constants import display


class Ball:
    def __init__(self, radius, vector):
        self.radius = radius
        self.vector = vector
        self.pos = [int(display.WIDTH / 2), int(display.HEIGHT / 2)]

    def move(self, rect_one, rect_two):

        if rect_one[0] <= self.pos[0] <= rect_one[0] + rect_one[2]:
            if rect_one[1] <= self.pos[1] <= rect_one[1] + rect_one[3]:
                self.vector[0] *= -1
        if rect_two[0] <= self.pos[0] <= rect_two[0] + rect_two[2]:
            if rect_two[1] <= self.pos[1] <= rect_two[1] + rect_two[3]:
                self.vector[0] *= -1
        if (self.pos[1] - self.radius) < 0 or (self.pos[1] + self.radius) > display.HEIGHT:
            self.vector[1] *= -1
        self.pos[0] += self.vector[0]
        self.pos[1] += self.vector[1]

    def reset(self):
        self.pos = [int(display.WIDTH / 2), int(display.HEIGHT / 2)]
