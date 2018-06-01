
###############################################################################
# Imports                                                                     #
###############################################################################

from course import Course
from lesson import Lesson
from starter import Starter
from exercise import InputOutputEx
from blurb import Blurb
import runner


###############################################################################
# Classes                                                                     #
###############################################################################

class EchoLesson(Lesson):

    name = "EchoLesson"

    class EchoAnythingEx(InputOutputEx):

        def __init__(self):
            super().__init__("Type 'echo <anything>' to print anything you want!")

        def verify(self, inp):
            return runner.get_stdout(inp), True

    class EchoExercise(InputOutputEx):

        def __init__(self, echo_goal):
            intro = "Print the following to stdout: {}".format(echo_goal)
            super().__init__(intro)
            self.echo_goal = echo_goal

        def verify(self, inp):
            return runner.match_stdout(inp, self.echo_goal)

    items = [Blurb("The `echo` command can be used to print to the screen. Try it now!"),
             EchoAnythingEx(),
             EchoExercise("bonjour"),
             EchoExercise("This sentence has more words")]

    def do_hello(self, line):
        print("EchoLesson says hello")


class BasicCourse(Course):

    name = "BasicCourse"

    lessons = Starter([EchoLesson])

    def do_hello(self, line):
        print("BasicCourse says hello")
