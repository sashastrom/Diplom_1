import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING  # Убедитесь, что эти импорты корректны


class TestIngredient:

    def test_get_price_correct(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88)
        assert ingredient.get_price() == 88

    def test_get_name_correct(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88)
        assert ingredient.get_name() == 'Соус с шипами Антарианского плоскоходца'

    @pytest.mark.parametrize(
        'ingredient_type, name, price, expected_type',
        [
            [INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Филе Люминесцентного тетраодонтимформа', 988, 'FILLING']
        ]
    )

    def test_get_type_correct(self, ingredient_type, name, price, expected_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_type