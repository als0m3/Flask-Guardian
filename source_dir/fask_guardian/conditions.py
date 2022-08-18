from .errors import *


def max_param(title, rule, target):
    if len(target) > rule:
        return error_must_be_less_than(title, str(rule))


def min_param(title, rule, target):
    if len(target) < rule:
        return error_must_be_more_than(title, str(rule))


def type_param(title, rule, target):
    if rule == "string" and type(target) is not str:
        return error_must_be_string(title)
