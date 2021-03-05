"Personal understanding: builder pattern emphasizes on the readability and user convenience, the code structure is not quite neat."

class BurgerBuilder:
    cheese = False
    pepperoni = False
    lettuce = False
    tomato = False

    def __init__(self, size):
        self.size = size

    def addPepperoni(self):
        self.pepperoni = True
        return self

    def addLecttuce(self):
        self.lettuce = True
        return self

    def addCheese(self):
        self.cheese = True
        return self

    def addTomato(self):
        self.tomato = True
        return self

    # builder
    def build(self):
        return Burger(self)

class Burger:
    def __init__(self, builder):
        self.size = builder.size
        self.cheese = builder.cheese
        self.pepperoni = builder.pepperoni
        self.lettuce = builder.lettuce
        self.tomato = builder.tomato


if __name__ == '__main__':
    # call builder
    b = BurgerBuilder(14).addPepperoni().addLecttuce().addTomato().build()
    print(b)
