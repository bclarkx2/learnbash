
###############################################################################
# Imports                                                                     #
###############################################################################

from course import Course
from lesson import Lesson
from starter import Starter
from exercise import InputOutputEx, QuestionEx
from runner import GenericIOBashCommand
from result import ErrorResult
from mistake import HintHandler
from blurb import Blurb


###############################################################################
# Classes                                                                     #
###############################################################################

class EchoLesson(Lesson):

    name = "EchoLesson"

    class EchoAnythingEx(InputOutputEx):

        def __init__(self):
            handler = HintHandler(3, "type \"echo hello\"")
            intro = "Type 'echo <anything>' to print anything you want!"
            super().__init__(handler, intro)

        def verify(self, inp):

            tokens = inp.split()
            if not tokens:
                return ErrorResult("Must enter something!")
            if tokens[0].lower() != "echo":
                return ErrorResult("Must use echo command!")
            if len(tokens) <= 1:
                return ErrorResult("Must provide arguments to echo!")

            out = GenericIOBashCommand(inp).run()
            return out.to_correct_result()

    class EchoExercise(InputOutputEx):

        def __init__(self, echo_goal):
            handler = HintHandler(3, "just do it!")
            intro = "Print the following to stdout: {}".format(echo_goal)
            super().__init__(handler, intro)
            self.echo_goal = echo_goal

        def verify(self, inp):
            out = GenericIOBashCommand(inp).run()
            if out.matches(self.echo_goal):
                return out.to_correct_result()
            else:
                return out.to_incorrect_result("Does not match!")

    items = [Blurb("The `echo` command can be used to print to the screen. Try it now!"),
             EchoAnythingEx(),
             EchoExercise("bonjour"),
             EchoExercise("This sentence has more words"),
             QuestionEx("What is the name of the command we just learned?", "echo"),
             Blurb("Congrats! You've finished the echo lesson!")]

    def do_hello(self, line):
        print("EchoLesson says hello")


class BasicCourse(Course):

    name = "BasicCourse"

    lessons = Starter([EchoLesson])
