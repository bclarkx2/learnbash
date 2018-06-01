
###############################################################################
# Imports                                                                     #
###############################################################################


###############################################################################
# Classes                                                                     #
###############################################################################

class InputOutputEx(object):

    def __init__(self, intro, outro=""):
        super().__init__()
        self.intro = intro
        self.outro = outro

    def do(self):
        print(self.intro)

        inp = input()

        output, result = self.verify(inp)

        if result:
            print(output)
            print("Correct!")
            if self.outro:
                print(self.outro)
        else:
            print("Incorrect, try again")
            self.do()

    def verify(self, inp):
        return "", False


class QuestionEx(InputOutputEx):

    def __init__(self, intro, answer, outro=""):
        super().__init__(intro, outro)
        self.answer = answer

    def verify(self, inp):
        return "", self.answer == inp
