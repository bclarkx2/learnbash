#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

import argparse
import importlib


###############################################################################
# CLI                                                                         #
###############################################################################

def check_learner(learner_name):
    return check_entity("learner", learner_name)


def check_entity(module_name, class_name):
    _module = importlib.import_module(module_name)
    _class = getattr(_module, class_name, None)
    return _class()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--learner",
                        default="Learner",
                        type=check_learner,
                        help="Learner to start")
    parser.add_argument("-c", "--course",
                        help="Name of course to start")
    parser.add_argument("-l", "--lesson",
                        help="Name of lesson to start")
    return parser.parse_args()


###############################################################################
# Main script                                                                 #
###############################################################################

def main():

    args = get_args()

    learner = args.learner

    if args.course:
        course_cls = learner.courses.by_name(args.course)
        if course_cls:
            course = course_cls()
            if args.lesson:
                lesson_cls = course.lessons.by_name(args.lesson)
                if lesson_cls:
                    lesson = lesson_cls()
                    lesson.start()
            course.start()
    learner.learn()


if __name__ == '__main__':
    main()
