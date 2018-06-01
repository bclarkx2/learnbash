#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

from cmd2 import Cmd

from basic import BasicCourse
from starter import Starter


###############################################################################
# Classes                                                                     #
###############################################################################

class Learner(Cmd):

    prompt = "learnBash>"
    intro = "let's learnBash"

    courses = Starter([BasicCourse])

    def __init__(self):
        Cmd.__init__(self)

    # Operations

    def learn(self):
        self.cmdloop()

    # Commands

    def do_quit(self, line):
        """Quit learnBash"""
        print("Quitting.")
        return True

    def do_courses(self, line):
        """List available courses"""
        print("Available courses:")
        print("\n".join(self.courses.names()))

    def do_start(self, line):
        """Start a course"""
        if not self.courses.start(line):
            print("No such course!")
