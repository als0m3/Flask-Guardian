from .errors import *
import re


def verify_email(target):
    regex = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    if re.search(regex, target):
        return True
    else:
        return False


def max_param(title, rule, target):
    if type(target) == str and len(target) > rule:
        return error_must_be_less_than(title, str(rule))
    elif type(target) == int and int(target) > rule:
        return error_must_be_less_than(title, str(rule))


def min_param(title, rule, target):
    if type(target) is str and len(target) < rule:
        return error_must_be_more_than(title, str(rule))
    elif type(target) is int and int(target) < rule:
        return error_must_be_more_than(title, str(rule))


def contains_param(title, rule, target):
    for item in rule:
        if item in target:
            return False
    return error_must_contain(title, rule)


def not_contains_param(title, rule, target):
    for item in rule:
        if item in target:
            return error_must_not_contain(title, rule)
    return False


def equal_param(title, rule, target):
    if rule == target:
        return False
    return error_must_equal(title, rule)


def not_equal_param(title, rule, target):
    if rule == target:
        return error_must_not_equal(title, rule)


def type_param(title, rule, target):
    if rule == "string" and type(target) is not str:
        return error_must_be_string(title)
    if rule == "integer" and type(target) is not int:
        return error_must_be_int(title)
    if rule == "email" and not verify_email(target):
        return error_must_be_email(title)
    if rule == "boolean" and type(target) is not bool:
        return error_must_be_boolean(title)
