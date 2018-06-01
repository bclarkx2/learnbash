#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

from cmd2 import Cmd

from basic import BasicCourse


###############################################################################
# Classes                                                                     #
###############################################################################

class Learner(Cmd):

    prompt = "learnBash>"
    intro = "let's learnBash"

    courses = [BasicCourse]

    def __init__(self):
        Cmd.__init__(self)

    # Data

    def course_names(self):
        return [c.name for c in self.courses]

    def course_by_name(self, name):
        for course in self.courses:
            if course.name == name:
                return course
        return None

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
        print("\n".join(self.course_names()))

    def do_start(self, line):
        """Start a course"""
        course_class = self.course_by_name(line)
        if course_class:
            course = course_class()
            course.start()
        else:
            print("No such course!")
