""" practicing a function calling a function"""

class Recipe:
    def __init__(self, recipe_id, recipe_name):
        self._recipe_id = recipe_id
        self._recipe_name = recipe_name

    def get_name(self):
        return self._recipe_name

    def get_id(self):
        return self._recipe_id


class CookingBot:
    def __init__(self):
        self._currently_cooking = {}

    def set_current_cooking(self, recipe_ob):
        recipe_id = recipe_ob.get_id()
        self._currently_cooking[recipe_id] = recipe_ob
        print("Currently cooking", recipe_ob.get_name())

chimichanga = Recipe(121,"Chimichanga")


CookingBot().set_current_cooking(chimichanga)