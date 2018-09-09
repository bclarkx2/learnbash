
###############################################################################
# Imports                                                                     #
###############################################################################

from cmd2 import Cmd


###############################################################################
# Classes                                                                     #
###############################################################################

class Lesson(Cmd):

    name = "GenericLesson"

    items = []

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "{}>".format(self.name)
        self.intro = "Starting lesson: {}".format(self.name)

    def num_exercises(cls):
        return sum(x.counts_as_exercise() for x in cls.items)

    def start(self):
        num_ex = self.num_exercises()
        ex_idx = 0
        for item in self.items:
            if item.counts_as_exercise():
                ex_idx += 1
                progress = "[Ex {}/{}]".format(
                    ex_idx,
                    num_ex)
                print(progress, end=" ")
            item.do()

    def do_hello(self):
        print("GenericLesson says hello")

    def do_quit(self):
        print("Quitting lesson: {}".format(self.name))
