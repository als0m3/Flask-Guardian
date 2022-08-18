def error_missing_ressource(target):
    return {"error": "Missing resource ['" + target + "']"}, 400


def error_must_be_string(target):
    return {"error": "Invalid resource ['" + target + "'], must be a string!"}, 400


def error_must_be_less_than(target, param):
    return {
        "error": "Invalid resource ['" + target + "'], must be less than " + param + "!"
    }, 400


def error_must_be_more_than(target, param):
    return {
        "error": "Invalid resource ['" + target + "'], must be more than " + param + "!"
    }, 400
