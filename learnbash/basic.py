
###############################################################################
# Imports                                                                     #
###############################################################################

from course import Course
from lesson import Lesson
from starter import Starter


###############################################################################
# Classes                                                                     #
###############################################################################

class BasicLesson1(Lesson):

    name = "BasicLesson1"

    def do_hello(self, line):
        print("BasicLesson1 says hello")


class BasicCourse(Course):

    name = "BasicCourse"

    lessons = Starter([BasicLesson1])

    def do_hello(self, line):
        print("BasicCourse says hello")
