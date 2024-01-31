import timeit
import matplotlib.pyplot as plt


class Item:
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.ratio = cost / calories


def greedy_menu(items: list[Item], budget: int) -> int:
    items.sort(key=lambda x: x.ratio, reverse=True)
    menu = {}
    for item in items:
        count = budget // item.cost
        if count > 0:
            menu[item.name] = count
        budget -= item.cost * count
    return menu


def dynamic_programming_menu(items: list[Item], budget: int):
    min_menu = [0] + [float("inf")] * budget
    last_menu_item = [0] * (budget + 1)

    for current_budget in range(1, budget + 1):
        for item in items:
            if (
                current_budget >= item.cost
                and min_menu[current_budget - item.cost] + 1 < min_menu[current_budget]
            ):
                min_menu[current_budget] = min_menu[current_budget - item.cost] + 1
                last_menu_item[current_budget] = item

    result_menu = {}
    current_sum = budget
    while current_sum > 0:
        item = last_menu_item[current_sum]
        result_menu[item.name] = result_menu.get(item.name, 0) + 1
        current_sum = current_sum - item.cost
    return result_menu


if __name__ == "__main__":
    menu = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    menu_db = []
    for i in menu.items():
        menu_db.append(Item(i[0], i[1]["cost"], i[1]["calories"]))

    print(greedy_menu(menu_db, 145))
    print(dynamic_programming_menu(menu_db, 145))
