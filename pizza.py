class Pizza:
    def __init__(self, pizzaName, pizzaType):
        self.pizzaName = pizzaName
        self.pizzaType = pizzaType



    def GetPizza(self, pizzaName):
        return pizzaName

    def GetPizzaType(self, pizzaType):
        return pizzaType


#inherited class of Pizza
class PizzaType(Pizza):
    def __init__(self, pizzaName, pizzaType):
        super().__init__(self, pizzaName, pizzaType)

    def GetPizzaType(self, pizzaType):
        return  pizzaType


