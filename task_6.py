class Item:
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.ratio = calories / cost


def greedy_menu(items: list[Item], budget: int) -> int:
    items.sort(key=lambda x: x.ratio, reverse=True)
    menu = {}
    for item in items:
        count = budget // item.cost
        if count > 0:
            menu[item.name] = count
        budget -= item.cost * count
    return menu


def dynamic_programming_max_calories(items: list[Item], budget: int) -> dict[str, int]:
    # Initialize dynamic programming tables
    max_calories = [0] * (budget + 1)
    last_item = [None] * (budget + 1)

    # Fill the dynamic programming tables
    for current_budget in range(1, budget + 1):
        for item in items:
            if current_budget >= item.cost and max_calories[current_budget - item.cost] + item.calories > max_calories[current_budget]:
                max_calories[current_budget] = max_calories[current_budget - item.cost] + item.calories
                last_item[current_budget] = item

    # Reconstruct the optimal set of dishes
    selected_dishes = {}
    current_budget = budget
    while last_item[current_budget] is not None:
        item = last_item[current_budget]
        selected_dishes[item.name] = selected_dishes.get(item.name, 0) + 1
        current_budget -= item.cost

    return selected_dishes


if __name__ == "__main__":
    menu = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    menu_db = []
    for i in menu.items():
        menu_db.append(Item(i[0], i[1]["cost"], i[1]["calories"]))

    greedy_result = greedy_menu(menu_db, 145)
    print(f"Жадібний алгоритм пропонує меню з:")
    for key, value in greedy_result.items():
        print(f"{key} - {value} шт.")
    dynamic_result = dynamic_programming_max_calories(menu_db, 145)
    print(f"\nДинамічний алгоритм пропонує меню з:")
    for key, value in dynamic_result.items():
        print(f"{key} - {value} шт.")
