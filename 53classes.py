class Robot:
    def introduce_self(self):
        print('My name is ' + self.name)
        print('I am ' + self.color+' in color')
        print('My weight is ' + self.weight)


r1=Robot()
r1.name="Tom"
r1.color="blue"
r1.weight='30 Kg'


r2=Robot()
r2.name="Jerry"
r2.color="black"
r2.weight='10 Kg'

r1.introduce_self()
r2.introduce_self()