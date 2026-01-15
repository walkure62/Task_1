import pytest
from praktikum.bun import Bun

class TestBun:
    @pytest.mark.parametrize("name, price, expected_name", [
    ("Кунжутная", 50.0, "Кунжутная"),
    ("Simple", 40.5, "Simple"),
    ("Сырная_2.0", 55.99, "Сырная_2.0")
])
    def test_bun_init_getter_name(self, name, price, expected_name):
        bun = Bun(name, price)

        assert bun.get_name() == expected_name
        assert bun.name == expected_name
    
    @pytest.mark.parametrize("name, price, expected_price", [
    ("Кунжутная", 50.0, 50.0),
    ("Simple", 40.5, 40.5),
    ("Сырная_2.0", 55.99, 55.99)
])    
    def test_bun_init_getter_price(self, name, price, expected_price):
        bun = Bun(name, price)

        assert bun.get_price() == expected_price
        assert bun.price == expected_price
    
    def test_bun_price_zero(self):
        bun = Bun("Волшебная", 0.0)
        assert bun.get_price() == 0.0
    
    def test_bun_getter_name_return_correct_types(self):
        bun = Bun("Кунжутная", 50.0)
        
        assert isinstance(bun.get_name(), str)
        
    def test_bun_getter_price_return_correct_types(self):
        bun = Bun("Кунжутная", 50.0)
        
        assert isinstance(bun.get_price(), float)