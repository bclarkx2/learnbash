
###############################################################################
# Imports                                                                     #
###############################################################################

from cmd2 import Cmd


###############################################################################
# Classes                                                                     #
###############################################################################

class Lesson(Cmd):

    name = "GenericLesson"

    exercises = []

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "{}>".format(self.name)
        self.intro = "Starting lesson: {}".format(self.name)

    def start(self):
        # self.cmdloop()
        for ex in self.exercises:
            ex.exercise()

    def do_hello(self):
        print("GenericLesson says hello")

    def do_quit(self):
        print("Quitting lesson: {}".format(self.name))
