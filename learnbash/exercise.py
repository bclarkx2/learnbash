
###############################################################################
# Imports                                                                     #
###############################################################################

from result import CorrectResult, ErrorResult


###############################################################################
# Base class                                                                  #
###############################################################################

class Exercise(object):

    def do(self):
        raise NotImplementedError("implement me!")


###############################################################################
# Classes                                                                     #
###############################################################################

class InputOutputEx(Exercise):

    def __init__(self, intro, outro=""):
        super().__init__()
        self.intro = intro
        self.outro = outro

    def do(self):
        print(self.intro)

        inp = input()

        result = self.verify(inp)

        if result.correct():
            print(result.output())
            print(result.message())
            print()
            if self.outro:
                print(self.outro)
        else:
            print(result.message())
            print()
            self.do()

    def verify(self, inp):
        pass


class QuestionEx(InputOutputEx):

    def __init__(self, intro, answer, outro=""):
        super().__init__(intro, outro)
        self.answer = answer

    def verify(self, inp):
        if self.answer == inp:
            return CorrectResult("Correct!")
        else:
            return ErrorResult("Wrong, try again!")
