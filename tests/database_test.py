from praktikum.database import Database
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    
    def test_available_buns_returns_usable_buns(self):
        db = Database()
        
        buns = db.available_buns()
        
        assert isinstance(buns, list)
        assert len(buns) > 0
        
        for bun in buns:
            assert bun.get_name() is not None
            assert bun.get_price() > 0
    
    def test_available_buns_can_be_used_in_burger(self):
        db = Database()
        burger = Burger()
        
        buns = db.available_buns()
        
        burger.set_buns(buns[0])
        assert burger.bun is not None
        assert burger.bun.get_name() == buns[0].get_name()
        assert burger.bun.get_price() == buns[0].get_price()
    
    def test_available_ingredients_returns_usable_ingredients(self):
        db = Database()
        
        ingredients = db.available_ingredients()
        
        assert isinstance(ingredients, list)
        assert len(ingredients) > 0
        
        for ingredient in ingredients:
            assert ingredient.get_name() is not None
            assert ingredient.get_price() > 0
            assert ingredient.get_type() in [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
    
    def test_available_ingredients_can_be_used_in_burger(self):
        db = Database()
        burger = Burger()
        
        ingredients = db.available_ingredients()
        
        burger.add_ingredient(ingredients[0])
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == ingredients[0].get_name()
        assert burger.ingredients[0].get_price() == ingredients[0].get_price()