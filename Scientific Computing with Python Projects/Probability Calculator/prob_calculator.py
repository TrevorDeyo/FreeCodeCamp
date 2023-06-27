import copy
import random
from collections import Counter

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for ball_color, amount in kwargs.items():
            self.contents.extend([ball_color] * amount)

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        counter = Counter(drawn_balls)
        success = True

        for ball, count in expected_balls.items():
            if counter[ball] < count:
                success = False
                break

        if success:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability