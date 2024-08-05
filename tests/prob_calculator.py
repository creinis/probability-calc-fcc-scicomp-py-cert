import random

class Hat:
    def draw(self, num):
        balls = []
        
        for _ in range(num):
            try:
                ball = random.choice(self.contents)
                self.contents.remove(ball)
                balls.append(ball)
            except IndexError:
                break
            
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
