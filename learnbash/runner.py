"""Executes bash commands"""

###############################################################################
# Imports                                                                     #
###############################################################################

import subprocess
from result import CorrectResult, ErrorResult


###############################################################################
# Classes                                                                     #
###############################################################################

class BashCommand(object):

    def run(self):
        pass


class GenericIOBashCommand(BashCommand):

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        try:
            raw = subprocess.check_output(["bash", "-c", self.command])
            processed = raw.decode().rstrip()
            out = BashValidOutput(processed)
            return out
        except subprocess.CalledProcessError as e:
            out = BashErrorOutput("<placeholder>")
            return out


class BashOutput(object):

    def output(self):
        pass

    def matches(self, target):
        pass

    def threw_bash_error(self):
        pass

    def is_valid(self):
        return not self.threw_bash_error()

    def to_correct_result(self):
        out = self.output()
        if self.is_valid():
            return CorrectResult(out)
        else:
            return ErrorResult("Bash error :(")

    def to_incorrect_result(self, msg):
        if self.is_valid():
            return ErrorResult(msg)
        else:
            return ErrorResult("Bash error :(")


class BashValidOutput(BashOutput):

    def __init__(self, output):
        super().__init__()
        self._output = output

    def output(self):
        return self._output

    def matches(self, target):
        return self._output == target

    def threw_bash_error(self):
        return False


class BashErrorOutput(BashOutput):

    def __init__(self, err):
        super().__init__()
        self._err = err

    def output(self):
        return self._err

    def matches(self, target):
        return False

    def threw_bash_error(self):
        return True


###############################################################################
# Utilities                                                                   #
###############################################################################

def match_stdout(inp, expected):
    try:
        stdout = get_stdout(inp)
        result = stdout == expected
        return stdout, result
    except UnexpectedBashException:
        return stdout, False


def get_stdout(inp):
    try:
        raw = subprocess.check_output(["bash", "-c", inp])
        processed = raw.decode().rstrip()
        return processed
    except subprocess.CalledProcessError as e:
        print("Ooops! Bash exception: {}".format(e))
        raise UnexpectedBashException()


###############################################################################
# Exceptions                                                                          #
###############################################################################

class UnexpectedBashException(Exception):
    pass
