class Recipe:
    def __init__(self, recipe_id, recipe_name, ingredients):
        self._ids = recipe_id
        self._name = recipe_name
        self._ingredients = ingredients


class CookingBot:
    def __init__(self, cuisine_mode):
        self._currently_cooking = None
        self._cuisine_mode = cuisine_mode

        print(f'Initializing CookingBot object to {self._cuisine_mode}.')


pasta = CookingBot("Pasta")

r1 = Recipe(42, "Poutine",
            {"water": "2tbsp", "beef broth": "20z", "unsalted  butter": "6 tbsp", "Russet potatoes": "2 pounds",
             "Frying oil": "Sufficient quantity", "pepper": "to taste"})
