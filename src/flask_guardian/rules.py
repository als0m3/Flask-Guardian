class Rules:
    def __init__(self):
        self.rules = dict()

    def Required(self):
        self.rules["required"] = True
        return self

    def String(self):
        self.rules["type"] = "string"
        return self

    def Email(self):
        self.rules["type"] = "email"
        return self

    def Integer(self):
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

    def Equal(self, value):
        self.rules["equal"] = value
        return self

    def notEqual(self, value):
        self.rules["notequal"] = value
        return self

    def Infos(self):
        return self.rules
