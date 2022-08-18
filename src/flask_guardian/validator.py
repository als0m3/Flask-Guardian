from flask import request

from .utils.conditions import *
from .rules import Rules


RULES = {
    "type": type_param,
    "max": max_param,
    "min": min_param,
    "contains": contains_param,
    "notcontains": not_contains_param,
    "equal": equal_param,
    "notequal": not_equal_param,
}


def parser(title, rules, target):
    for rule in RULES:
        if rule in rules:
            response = RULES[rule](title, rules[rule], target)
            if response:
                return response


def Validator(parameters):
    def inner_decorator(f):
        def wrapped(*args, **kwargs):
            body = request.get_json()
            for title in parameters:
                rules = parameters[title].Infos()
                if "required" in rules and title not in body:
                    return error_missing_ressource(title)
                elif title in body:
                    result = parser(title, rules, body[title])
                    if result:
                        return result
            return f(*args, **kwargs)

        return wrapped

    return inner_decorator
