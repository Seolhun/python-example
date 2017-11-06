class Greeter:
    visitor = None
    count = 0

    def __init__(self, boss):
        self.boss = boss

    def enters(self, visitor):
        self.visitor = visitor
        return visitor

    def greet(self):
        if self.visitor is not None and self.count == 0:
            self.count += 1
            if self.visitor == self.boss:
                return 'Very very welcome, {}'.format(self.boss)
            return 'Welcome, {}'.format(self.visitor)
        return None


g = Greeter('Chuck')
g.enters('John')
print(g.greet())
