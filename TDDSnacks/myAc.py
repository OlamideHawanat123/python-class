class MyAc:

    is_on = False
    def init(self, name: str):
        self.name = name
        self.is_on = False

    def isOn(self):
        return self.is_on

    def turn_on(self):
        if self.is_on:
            self.is_on = True
        else:
            return f'{self.name} is already turned on'

