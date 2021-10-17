class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print('My name is ' + self.name)
        print('I am ' + self.color+' in color')
        print('My weight is ' + self.weight)


r1 = Robot("Tom", "blue", "40 kg")
r2 = Robot("Jerry", "brown", "10 kg")

r1.introduce_self()
r2.introduce_self()
