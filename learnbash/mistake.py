
###############################################################################
# Imports                                                                     #
###############################################################################


###############################################################################
# Base class                                                                  #
###############################################################################

class MistakeHandler(object):

    def form_message(self, history):
        raise NotImplementedError("implement!")


###############################################################################
# Concrete implementations                                                    #
###############################################################################

class NoHandler(MistakeHandler):

    def form_message(self, history):
        return "Incorrect. Try again!"


class HintHandler(MistakeHandler):

    def __init__(self, mistake_limit, hint):
        super().__init__()
        self._mistake_limit = mistake_limit
        self._hint = hint

    def form_message(self, history):
        if history.attempts() >= self._mistake_limit:
            return "Incorrect. Hint: " + self._hint
        else:
            most_recent = history.most_recent()
            return most_recent.message()
