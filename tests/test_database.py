from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_buns_count(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_buns_names(self):
        db = Database()
        buns = db.available_buns()
        bun_names = [bun.get_name() for bun in buns]
        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names

    def test_total_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_sauces_available(self):
        db = Database()
        ingredients = db.available_ingredients()
        sauces = [ingredient for ingredient in ingredients if ingredient.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    def test_sauces_names(self):
        db = Database()
        ingredients = db.available_ingredients()
        sauces = [ingredient for ingredient in ingredients if ingredient.get_type() == INGREDIENT_TYPE_SAUCE]
        sauce_names = [ingredient.get_name() for ingredient in sauces]
        assert "hot sauce" in sauce_names
        assert "sour cream" in sauce_names
        assert "chili sauce" in sauce_names

    def test_fillings_available(self):
        db = Database()
        ingredients = db.available_ingredients()
        fillings = [ingredient for ingredient in ingredients if ingredient.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3

    def test_fillings_names(self):
        db = Database()
        ingredients = db.available_ingredients()
        fillings = [ingredient for ingredient in ingredients if ingredient.get_type() == INGREDIENT_TYPE_FILLING]
        filling_names = [ingredient.get_name() for ingredient in fillings]
        assert "cutlet" in filling_names
        assert "dinosaur" in filling_names
        assert "sausage" in filling_names

    def test_ingredient_prices(self):
        db = Database()
        ingredients = db.available_ingredients()
        prices = {ingredient.get_name(): ingredient.get_price() for ingredient in ingredients}
        assert prices["hot sauce"] == 100
        assert prices["sour cream"] == 200
        assert prices["cutlet"] == 100
        assert prices["dinosaur"] == 200