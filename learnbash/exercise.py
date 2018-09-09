
###############################################################################
# Imports                                                                     #
###############################################################################

from result import CorrectResult, ErrorResult
from history import ExerciseHistory
from mistake import HintHandler, NoHandler


###############################################################################
# Base class                                                                  #
###############################################################################

class Exercise(object):

    def do(self):
        raise NotImplementedError("implement me!")

    def counts_as_exercise(self):
        return True


###############################################################################
# Classes                                                                     #
###############################################################################

class InputOutputEx(Exercise):

    def __init__(self, handler, intro, outro=""):
        super().__init__()
        self.intro = intro
        self.outro = outro
        self._history = ExerciseHistory()
        self._handler = handler

    def do(self):
        print(self.intro)

        inp = input()

        result = self.verify(inp)
        self.record(result)

        if result.correct():
            print(result.output())
            print(result.message())
            print()
            if self.outro:
                print(self.outro)
        else:
            print(self.mistake_message())
            print()
            self.do()

    # delegate recording to history object
    def record(self, result):
        self._history.record(result)

    def mistake_message(self):
        return self._handler.form_message(self._history)

    def verify(self, inp):
        pass


class QuestionEx(InputOutputEx):

    def __init__(self, intro, answer, outro="", mistake_limit=0, hint=""):
        if hint and mistake_limit:
            handler = HintHandler(mistake_limit, hint)
        else:
            handler = NoHandler()
        super().__init__(handler, intro, outro)
        self.answer = answer

    def verify(self, inp):
        if self.answer == inp:
            return CorrectResult("")
        else:
            return ErrorResult("Wrong, try again!")
