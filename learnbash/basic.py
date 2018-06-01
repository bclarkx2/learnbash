
###############################################################################
# Imports                                                                     #
###############################################################################

from course import Course
from lesson import Lesson
from starter import Starter
from exercise import InputOutputEx

import subprocess


###############################################################################
# Classes                                                                     #
###############################################################################

class EchoLesson(Lesson):

    name = "EchoLesson"

    class EchoExercise(InputOutputEx):

        def __init__(self, echo_goal):
            intro = "Print the following to stdout: {}".format(echo_goal)
            super().__init__(intro)
            self.echo_goal = echo_goal

        def verify(self, inp):
            raw = subprocess.check_output(["bash", "-c", inp])
            processed = raw.decode().rstrip()
            return processed == self.echo_goal

    exercises = [EchoExercise("bonjour")]

    def do_hello(self, line):
        print("EchoLesson says hello")


class BasicCourse(Course):

    name = "BasicCourse"

    lessons = Starter([EchoLesson])

    def do_hello(self, line):
        print("BasicCourse says hello")
