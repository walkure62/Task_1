import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *

    
class TestBurger:
    
    def test_init_empty_burger(self):
        burger = Burger()
        
        assert burger.bun is None
        assert len(burger.ingredients) == 0
    
    def test_set_buns(self):
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Сырная"
        bun_mock.get_price.return_value = 50.89
        
        burger = Burger()
        burger.set_buns(bun_mock)
        
        assert burger.bun == bun_mock
        assert burger.bun.get_name() == "Сырная"
        
    def test_add_ingredient_success(self):
        ingredient_mock = Mock()
        ingredient_mock.get_price.return_value = 20.0
        
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_mock
    
    def test_remove_ingredient_valid_index(self):
        ing1 = Mock()
        ing2 = Mock()
        
        burger = Burger()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ing2
            
    def test_move_ingredient_valid(self):
        ing1 = Mock(name="Котлета")
        ing2 = Mock(name="Сыр")
        ing3 = Mock(name="Помидор")
        
        burger = Burger()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)
        
        burger.move_ingredient(1, 0)
        
        assert len(burger.ingredients) == 3
        assert burger.ingredients[0] == ing2
        assert burger.ingredients[1] == ing1
        assert burger.ingredients[2] == ing3
        
    def test_get_price_without_bun_raises_error(self):
        ing1 = Mock()
        ing1.get_price.return_value = 10.0
        
        burger = Burger()
        burger.add_ingredient(ing1)
        
        with pytest.raises(AttributeError, match=r"NoneType' object has no attribute 'get_price'"): 
            burger.get_price()
    
    def test_get_price_with_bun_success(self):
        bun_mock = Mock(get_price=lambda: 50.0)
        ing1 = Mock(get_price=lambda: 15.0)
        
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ing1)
        
        assert burger.get_price() == 115.0
        
    def test_get_receipt(self):
        bun = Bun('Кунжутная', 56.92)
        ing1 = Ingredient(INGREDIENT_TYPE_FILLING, 'Котлета', 100.00)
        ing2 = Ingredient(INGREDIENT_TYPE_SAUCE, 'Кетчуп', 30.55)
        
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        receipt = burger.get_receipt()
        
        assert '==== Кунжутная ====' in receipt
        assert '= filling Котлета =' in receipt
        assert '= sauce Кетчуп =' in receipt
        assert 'Price: 244.39' in receipt