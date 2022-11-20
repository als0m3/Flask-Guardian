def error_missing_ressource(target):
    return {"error": "Missing resource ['" + target + "']"}, 400


def error_must_be_string(target):
    return {"error": "Invalid resource ['" + target + "'], must be a string !"}, 400


def error_must_be_email(target):
    return {"error": "Invalid resource ['" + target + "'], must be an email !"}, 400


def error_must_be_int(target):
    return {"error": "Invalid resource ['" + target + "'], must be an integer !"}, 400


def error_must_be_boolean(target):
    return {"error": "Invalid resource ['" + target + "'], must be a boolean !"}, 400


def error_must_be_less_than(target, param):
    return {
        "error": "Invalid resource ['"
        + target
        + "'], must be less than "
        + param
        + " !"
    }, 400


def error_must_be_more_than(target, param):
    return {
        "error": "Invalid resource ['"
        + target
        + "'], must be more than "
        + param
        + " !"
    }, 400


def error_must_contain(target, param):
    return {
        "error": "Invalid resource ['"
        + target
        + "'], must contain ['"
        + "' / '".join(param)
        + "'] !"
    }, 400


def error_must_not_contain(target, param):
    return {
        "error": "Invalid resource ['"
        + target
        + "'], must not contain ['"
        + "' / '".join(param)
        + "'] !"
    }, 400


def error_must_equal(target, param):
    return {
        "error": "Invalid resource ['" + target + "'], must equal ['" + param + "'] !"
    }, 400


def error_must_not_equal(target, param):
    return {
        "error": "Invalid resource ['"
        + target
        + "'], must not equal ['"
        + param
        + "'] !"
    }, 400
