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
        result = stdout == expected
        return stdout, result
    except subprocess.CalledProcessError:
        return stdout, False


def get_stdout(inp):
    raw = subprocess.check_output(["bash", "-c", inp])
    processed = raw.decode().rstrip()
    return processed
