
###############################################################################
# Imports                                                                     #
###############################################################################


###############################################################################
# Classes                                                                     #
###############################################################################

class Blurb(object):

    def __init__(self, msg):
        self.msg = msg

    def do(self):
        print(self.msg)

    def counts_as_exercise(self):
        return False
