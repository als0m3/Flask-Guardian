class Rules:
    def __init__(self):
        self.rules = dict()

    def isRequired(self):
        self.rules["required"] = True
        return self

    def isString(self):
        self.rules["type"] = "string"
        return self

    def isBoolean(self):
        self.rules["type"] = "boolean"
        return self

    def isEmail(self):
        self.rules["type"] = "email"
        return self

    def isInteger(self):
        self.rules["type"] = "integer"
        return self

    def Min(self, value):
        self.rules["min"] = value
        return self

    def Max(self, value):
        self.rules["max"] = value
        return self

    def Contains(self, value):
        self.rules["contains"] = value
        return self

    def notContains(self, value):
        self.rules["notcontains"] = value
        return self

    def isEqual(self, value):
        self.rules["equal"] = value
        return self

    def isNotEqual(self, value):
        self.rules["notequal"] = value
        return self

    def Infos(self):
        return self.rules
