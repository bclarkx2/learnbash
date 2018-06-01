"""Executes bash commands"""

###############################################################################
# Imports                                                                     #
###############################################################################

import subprocess


###############################################################################
# Utilities                                                                   #
###############################################################################

def match_stdout(inp, expected):
    try:
        stdout = get_stdout(inp)
        print("stdout: {}".format(stdout))
        print("echo goal: {}".format(stdout))
        return stdout == expected
    except subprocess.CalledProcessError:
        return False


def get_stdout(inp):
    raw = subprocess.check_output(["bash", "-c", inp])
    processed = raw.decode().rstrip()
    return processed
