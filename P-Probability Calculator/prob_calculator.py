import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for x in range(value):
                self.contents.append(key)

    def draw(self, amount):
        newList = []
        if amount > len(self.contents):
            return self.contents
        else:
            for x in range(amount):
                newList.append(self.contents.pop(random.randrange(len(self.contents))))
        return newList       
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    timesHappened = 0

    for z in range(num_experiments):
        copiedHat = copy.deepcopy(hat)
        newList = copiedHat.draw(num_balls_drawn)
        success = True

        for key, value in expected_balls.items():
            if newList.count(key) < value:
                success = False
                break
        if success:
            timesHappened += 1

    print("Times happened: " + str(timesHappened))
    return (timesHappened / num_experiments)