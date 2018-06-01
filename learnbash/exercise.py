
###############################################################################
# Imports                                                                     #
###############################################################################


###############################################################################
# Classes                                                                     #
###############################################################################

class InputOutputEx(object):

    def __init__(self, intro):
        super().__init__()
        self.intro = intro

    def exercise(self):
        print(self.intro)

        inp = input()

        if self.verify(inp):
            print("Correct!")
        else:
            print("Incorrect, try again")
            self.exercise()

    def verify(self, inp):
        return False
