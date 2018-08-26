
###############################################################################
# Imports                                                                     #
###############################################################################

from cmd2 import Cmd
from starter import Starter


###############################################################################
# Classes                                                                     #
###############################################################################

class Course(Cmd):

    name = "GenericCourse"

    lessons = Starter([])

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

    def do_lessons(self, line):
        """List lessons in course"""
        for pos, name in enumerate(self.lessons.names(), start=1):
            print("{}. {}".format(pos, name))

    def do_start(self, line):
        if not self.lessons.start(line):
            print("No such lesson!")

    def complete_start(self, text, line, begidx, endidx):
        return self.lessons.matching(text)
