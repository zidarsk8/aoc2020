import aoc21_data

from typing import List, Tuple, Set, Dict


Food = List[Tuple[Set[str], Set[str]]]


def parse(text: str) -> Food:
    food = []
    for line in text.splitlines():
        ingredits_part, allergen_part = line.split(" (contains ")
        ingredits = ingredits_part.split()
        allergens = allergen_part[:-1].split(", ")
        assert len(allergens) == len(set(allergens))
        assert len(ingredits) == len(set(ingredits))
        food.append((set(ingredits), set(allergens)))
    return food


def test_parse():
    food = parse(aoc21_data.test_data)
    assert food[0][1] == {"dairy", "fish"}

    food = parse(aoc21_data.data)
    assert food[0][1] == {"nuts", "sesame"}


def get_all_allergens(food: Food) -> Set[str]:
    return food[0][1].union(*[allergens for _, allergens in food])


def test_get_all_allergens():
    food = parse(aoc21_data.test_data)
    assert get_all_allergens(food) == {"dairy", "fish", "soy"}


def get_ingredients_for_allergen(food: Food, allergen: str) -> Dict[str, Set[str]]:

    for ingredits, allergens in food:
        print(ingredits, allergens)

    return {}


def reduce(food: Food) -> Dict[str, Set[str]]:
    allergen_map: Dict[str, Set[str]] = {}
    for ingredits, allergens in food:
        for allergen in allergens:
            if allergen not in allergen_map:
                allergen_map[allergen] = set(ingredits)
            else:
                allergen_map[allergen] &= ingredits

    singles: Dict[str, str] = {}
    while allergen_map:
        new_singles = {
            allergen: ingredients.pop()
            for allergen, ingredients in allergen_map.items()
            if len(ingredients) == 1
        }
        for single_allergen, single_ingredient in new_singles.items():
            del allergen_map[single_allergen]
        for single_allergen, single_ingredient in new_singles.items():
            for allergen, ingredients in allergen_map.items():
                allergen_map[allergen] -= {single_ingredient}
        singles.update(new_singles)

    return singles


def count_other_ingredients(food):
    allergen_map = reduce(food)
    alergic_ingredients = set(allergen_map.values())
    return sum(len(ingredients - alergic_ingredients) for ingredients, _ in food)


def canonical(food):
    allergen_map = reduce(food)
    return ",".join(ingredient for _, ingredient in sorted(allergen_map.items()))


def test_reduce():
    food = parse(aoc21_data.test_data)
    reduced = reduce(food)

    assert reduced["fish"] == "sqjhc"


def test_count():
    food = parse(aoc21_data.test_data)
    assert count_other_ingredients(food) == 5
    food = parse(aoc21_data.data)
    assert count_other_ingredients(food) == 2595


def test_canonical():
    food = parse(aoc21_data.test_data)
    assert canonical(food) == "mxmxvkd,sqjhc,fvjkl"
    food = parse(aoc21_data.data)

    print(canonical(food))
    assert canonical(food) == ""
