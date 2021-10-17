class Mammal:
    def feature1(self):
        print("Gives birth directly to babies")

    def feature2(self):
        print("Have hairs")
    def feature3(self):
        print("Mammary Gland")

# Dog is a child of Mammal
class Dog(Mammal):  # inheritance #created Subclass Dog #Got characteristics of Mammal
    def feature4(self):
        print("Have 4 legs")

    def feature5(self):
        print("Good sense of smelling and hearing")

# c is grand child of A and child of B


class BullDog(Dog):  # it can access the characteristics of both B an A
    def feature6(self):
        print("Angry in nature")

    def feature7(self):
        print("Bulky looks")


mammal = Mammal()
mammal.feature1()
mammal.feature2()
mammal.feature3()

dog = Dog()
dog.feature1()
dog.feature2()
dog.feature3()
dog.feature4()
dog.feature5()

bulldog = BullDog()
bulldog.feature1()
bulldog.feature2()
bulldog.feature3()
bulldog.feature4()
bulldog.feature5()
bulldog.feature6()
bulldog.feature7()