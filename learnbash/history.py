
###############################################################################
# Imports                                                                     #
###############################################################################


###############################################################################
# Base class                                                                  #
###############################################################################

class ExerciseHistory(object):

    def __init__(self):
        super().__init__()
        self._results = []

    def record(self, result):
        self._results.append(result)

    def most_recent(self):
        return self._results[-1]

    def attempts(self):
        return len(self._results)
