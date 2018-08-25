
###############################################################################
# Imports                                                                     #
###############################################################################


###############################################################################
# Base Class                                                                  #
###############################################################################

class ExerciseResult(object):

    def correct(self):
        pass

    def output(self):
        pass

    def message(self):
        pass


###############################################################################
# Concrete Results                                                            #
###############################################################################

class CorrectResult(ExerciseResult):

    def __init__(self, output):
        super().__init__()
        self._output = output

    def correct(self):
        return True

    def output(self):
        return self._output

    def message(self):
        return "Correct!"


class ErrorResult(ExerciseResult):

    def __init__(self, msg):
        super().__init__()
        self._msg = msg

    def correct(self):
        return False

    def output(self):
        return ""

    def message(self):
        return self._msg
