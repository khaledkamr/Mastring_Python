from random import *

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    for i in range(num_experiments):

        balls = hat.draw(num_balls_drawn)
        m = 0

        for ball in expected_balls:        
            c = 0
            if (ball in balls):
                count = 0
                for j in balls:
                    if (j == ball):
                        count += 1

                if(count == expected_balls[ball]):
                    c += 1
            
            if(c == len(expected_balls)):
                m += 1   

    return m/num_experiments

class Hat:

    def __init__(self, *colors):

        self.contents = []

        for color in colors:
            c, i = color.split("=")
            for j in range(int(i)):
                self.contents.append(c)

    def draw(self, n):

        if n > len(self.contents):
            return self.contents

        balls = []
        size = len(self.contents) - 1

        for i in range(n):
            drawnBall = self.contents[randint(0, size)]
            balls.append(drawnBall)
            self.contents.remove(drawnBall)
            size -= 1

        return balls

hat = Hat("black=6", "red=4", "green=3")
probability = experiment(hat, {"red":2,"green":1}, 5, 2000)
print(probability)