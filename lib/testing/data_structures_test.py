import io
import sys
import pytest
from data_structures import (get_names, get_spiciest_foods, print_spicy_foods,
                             create_spicy_food, get_spicy_food_by_cuisine,
                             print_spiciest_foods, get_average_heat_level)

class TestDataStructures:

    SPICY_FOODS = [
        {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
        {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
    ]

    def test_get_names(self):
        assert get_names(TestDataStructures.SPICY_FOODS) == ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']

    def test_get_spiciest_foods(self):
        for food in get_spiciest_foods(TestDataStructures.SPICY_FOODS):
            assert food["heat_level"] > 5

    def test_print_spicy_foods(self, capsys):
        print_spicy_foods(TestDataStructures.SPICY_FOODS)
        captured = capsys.readouterr()
        expected_output = "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\n" \
                          "Buffalo Wings (American) | Heat Level: 🌶🌶🌶\n" \
                          "Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶\n"
        assert captured.out == expected_output

    def test_get_spicy_food_by_cuisine(self):
        assert get_spicy_food_by_cuisine(TestDataStructures.SPICY_FOODS, "American") == {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3
    }


    def test_print_spiciest_foods(self, capsys):
        print_spiciest_foods(TestDataStructures.SPICY_FOODS)
        captured = capsys.readouterr()
        assert captured.out == "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\n" \
                               "Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶\n"

    def test_get_average_heat_level(self):
        assert get_average_heat_level(TestDataStructures.SPICY_FOODS) == 6

    def test_create_spicy_food(self):
        new_spicy_foods = create_spicy_food(
            TestDataStructures.SPICY_FOODS,
            {"name": "Griot", "cuisine": "Haitian", "heat_level": 10}
        )
        assert new_spicy_foods[-1] == {"name": "Griot", "cuisine": "Haitian", "heat_level": 10}
