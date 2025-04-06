from unittest.mock import Mock
from praktikum.burger import Burger, Bun
from praktikum.database import Database
import praktikum.ingredient_types as ingredient_types


class TestSetBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun('white bun', 200.0)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'cutlet'
        mock_ingredient.get_price.return_value = 100.0
        mock_ingredient.get_type.return_value = ingredient_types.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        ingredient = burger.ingredients[0]
        assert ingredient.get_name() == 'cutlet'
        assert ingredient.get_price() == 100.0
        assert ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_FILLING

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        db = Database()
        burger.set_buns(db.available_buns()[1])
        burger.add_ingredient(db.available_ingredients()[0])
        burger.add_ingredient(db.available_ingredients()[3])
        burger.add_ingredient(db.available_ingredients()[4])
        assert burger.ingredients[0].get_name() == 'hot sauce'
        assert burger.ingredients[1].get_name() == 'cutlet'
        assert burger.ingredients[2].get_name() == 'dinosaur'

        burger.move_ingredient(1, 0)
        assert burger.ingredients[0].get_name() == 'cutlet'
        assert burger.ingredients[1].get_name() == 'hot sauce'
        assert burger.ingredients[2].get_name() == 'dinosaur'

    def test_get_price(self):
        burger = Burger()
        db = Database()
        burger.set_buns(db.available_buns()[1])
        burger.add_ingredient(db.available_ingredients()[0])
        burger.add_ingredient(db.available_ingredients()[3])
        assert burger.get_price() == 600.0

    def test_get_receipt(self):
        burger = Burger()
        db = Database()
        burger.set_buns(db.available_buns()[1])
        burger.add_ingredient(db.available_ingredients()[0])
        burger.add_ingredient(db.available_ingredients()[3])

        expected_receipt = "(==== white bun ====)\n" \
                           "= sauce hot sauce =\n" \
                           "= filling cutlet =\n" \
                           "(==== white bun ====)\n\n" \
                           "Price: 600"
        assert burger.get_receipt() == expected_receipt