import pytest
from praktikum.database import Database
from praktikum.ingredient_types import *
    
class TestDatabase:
    
    def test_init_buns_count(self):
        db = Database()
        
        assert len(db.buns) == 3
        assert db.buns[0].get_name() == "black bun"
        assert db.buns[0].get_price() == 100
        assert db.buns[1].get_name() == "white bun" 
        assert db.buns[1].get_price() == 200
        assert db.buns[2].get_name() == "red bun"
        assert db.buns[2].get_price() == 300
        
    def test_init_ingredients_count(self):
        db = Database()
        
        assert len(db.ingredients) == 6
        
        sauces = [ing for ing in db.ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3
        assert sauces[0].get_name() == "hot sauce"
        assert sauces[1].get_name() == "sour cream" 
        assert sauces[2].get_name() == "chili sauce"
        
        fillings = [ing for ing in db.ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3
        assert fillings[0].get_name() == "cutlet"
        assert fillings[1].get_name() == "dinosaur"
        assert fillings[2].get_name() == "sausage"
        
    def test_available_buns_returns_all_buns(self):
        db = Database()
        
        buns = db.available_buns()
        
        assert len(buns) == 3
        assert buns == db.buns
        assert [bun.get_name() for bun in buns] == ["black bun", "white bun", "red bun"]
    
    def test_available_ingredients_returns_all_ingredients(self):
        db = Database()
        
        ingredients = db.available_ingredients()
        
        assert len(ingredients) == 6
        assert ingredients == db.ingredients
        
        sauce_names = ["hot sauce", "sour cream", "chili sauce"]
        filling_names = ["cutlet", "dinosaur", "sausage"]
        
        names = [ing.get_name() for ing in ingredients]
        assert sauce_names in names or all(s in names for s in sauce_names)
        assert filling_names in names or all(f in names for f in filling_names)
    
        
    @pytest.mark.parametrize("method", ["available_buns", "available_ingredients"])
    def test_methods_return_lists(self, method):
        db = Database()
        
        result = getattr(db, method)()
        assert isinstance(result, list)
        assert len(result) > 0
