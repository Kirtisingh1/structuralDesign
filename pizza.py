class Pizza:
    def get_description(self):
        return "Basic Pizza"

    def get_cost(self):
        return 5.0

class CheeseDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description() + ", Cheese"

    def get_cost(self):
        return self.pizza.get_cost() + 1.5

# Usage
pizza = Pizza()
cheese_pizza = CheeseDecorator(pizza)
print(cheese_pizza.get_description())  # Basic Pizza, Cheese
print(cheese_pizza.get_cost())  # 6.5
