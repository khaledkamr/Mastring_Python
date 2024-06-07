from random import *
from copy import *

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    count = 0
    for i in range(num_experiments):

        expected_copy = deepcopy(expected_balls)
        hat_copy = deepcopy(hat)
        colors_gotten = hat_copy.draw(num_balls_drawn)

        for color in colors_gotten:
            if(color in expected_copy):
                expected_copy[color] -= 1

        if(all(x <= 0 for x in expected_copy.values())):
            count += 1
        
    return count/num_experiments

class Hat:

    def __init__(self, **colors):

        self.contents = []

        for color, n in colors.items():
            for i in range(n):
                self.contents.append(color)

    def draw(self, n):

        if (n > len(self.contents)):
            return self.contents

        balls = []

        for i in range(n):
            size = len(self.contents) - 1
            drawnBall = self.contents[randint(0, size)]
            balls.append(drawnBall)
            self.contents.remove(drawnBall)

        return balls

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat, {"red":2,"green":1}, 5, 2000)
print(probability)