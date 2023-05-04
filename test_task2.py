import pytest
from task2 import count_cakes

def test_cakes_with_zero_amounts():
    recipe = {'flour': 500, 'sugar': 0, 'eggs': 1}
    available = {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}
    with pytest.raises(ZeroDivisionError, match="Ошибка: Ингридиент sugar в рецепте имеет нулевое значение."):
            count_cakes(recipe, available)


def test_cakes_with_enough_ingredients():
    recipe = {'flour': 500, 'sugar': 200, 'eggs': 1}
    available = {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}
    assert count_cakes(recipe, available) == 2


# проверить случай когда в доступных отсутствует один ингридиент из рецепта


# проверить случай когда одного из доступных ингридиентов не достаточно для изготовления торта


# проверить случай когда доступно сильно больше ингридиентов


# проверить случай когда один или несколько доступных ингридиентов равны 0