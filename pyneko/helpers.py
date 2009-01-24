import os.path
from subprocess import Popen

def compile(filename):
    exitcode = Popen(['nekoc', filename]).wait()
    return exitcode == 0

def run(filename):
    exitcode = Popen(['neko', filename]).wait()
    return exitcode == 0

def compile_and_run(filename):
    if compile(filename):
        run(os.path.splitext(filename)[0])

