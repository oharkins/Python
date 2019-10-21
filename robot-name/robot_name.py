import random
import string


def randname():
    return random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)


class Robot(object):

    def __init__(self):

        self.name = randname()
        self.reset()

    def reset(self):
        self.name = randname()
