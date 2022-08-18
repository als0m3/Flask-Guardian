class Rules:
    def __init__(self):
        self.rules = dict()

    def Required(self):
        self.rules["required"] = True
        return self

    def String(self):
        self.rules["type"] = "string"
        return self

    def Min(self, value):
        self.rules["min"] = value
        return self

    def Max(self, value):
        self.rules["max"] = value
        return self

    def Infos(self):
        return self.rules
