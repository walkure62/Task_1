import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *

class TestIngredient:
    
    @pytest.mark.parametrize("ingredient_type, name, price, expected_type, expected_name, expected_price", [
        (INGREDIENT_TYPE_FILLING, "Котлета", 100.0, "FILLING", "Котлета", 100.0),
        (INGREDIENT_TYPE_SAUCE, "Кетчуп", 20.5, "SAUCE", "Кетчуп", 20.5),
        (INGREDIENT_TYPE_FILLING, "Сыр", 30.75, "FILLING", "Сыр", 30.75),
        (INGREDIENT_TYPE_SAUCE, "Майонез", 25.0, "SAUCE", "Майонез", 25.0),
    ])
    def test_ingredient_init_getters(self, ingredient_type, name, price, 
                                   expected_type, expected_name, expected_price):
        ingredient = Ingredient(ingredient_type, name, price)
        
        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price
        
        assert ingredient.type == expected_type
        assert ingredient.name == expected_name
        assert ingredient.price == expected_price
    
    def test_correct_return_types(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Котлета", 100.5)
        
        assert isinstance(ingredient.get_type(), str)
        assert isinstance(ingredient.get_name(), str)
        assert isinstance(ingredient.get_price(), float)