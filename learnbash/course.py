
###############################################################################
# Imports                                                                     #
###############################################################################

from cmd2 import Cmd


###############################################################################
# Classes                                                                     #
###############################################################################

class Course(Cmd):

    name = "GenericCourse"

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "{}>".format(self.name)
        self.intro = "Starting {}".format(self.name)

    def start(self):
        self.cmdloop()

    def do_hello(self, line):
        print("Course says hello")

    def do_quit(self, line):
        print("Quitting course: {}".format(self.name))
        return True
