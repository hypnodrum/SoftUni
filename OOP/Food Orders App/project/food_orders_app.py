from project.meals.meal import Meal
from project.client import Client


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number):

        client = Client(client_phone_number)
        for c in self.clients_list:
            if c.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        valid_meals = ["Starter", "MainDish", "Dessert"]
        for meal in meals:
            if type(meal).__name__ in valid_meals:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        return ["\n".join(meal.details() for meal in self.menu)]

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        pass

    def cancel_order(self, client_phone_number):
        pass

    def finish_order(self, client_phone_number):
        pass

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
