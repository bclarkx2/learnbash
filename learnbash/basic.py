
###############################################################################
# Imports                                                                     #
###############################################################################

from course import Course


###############################################################################
# Classes                                                                     #
###############################################################################

class BasicCourse(Course):

    name = "BasicCourse"

    def do_hello(self, line):
        print("BasicCourse says hello")
