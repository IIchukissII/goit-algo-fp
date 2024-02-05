# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком
- Релізовано реверсування однозв'язного списку, змінюючи посилання між вузлами
- Реалізовано алгоритм сортування для однозв'язного списку
- Реалізовано об'єднання двох відсортованих однозв'язних списків в один відсортований список.

# Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії
- Програма візуалізує фрактал “дерево Піфагора”, і користувач має можливість вказати рівень рекурсії.
  Викликається з консолі (приклад виклику - python task_2.py -d *рівень_рекурсії*)
  ![pythagoras](https://github.com/IIchukissII/goit-algo-fp/assets/133657307/7174a9bd-7ee9-424c-a5a6-378a3ef84e55)

# Завдання 3. Дерева, алгоритм Дейкстри
- Реалізовано алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу
![task_3](https://github.com/IIchukissII/goit-algo-fp/assets/133657307/5e9b8a35-9601-4c46-9318-84754456eb6d)


- В прикладі граф створюється за допомогою словника: 
graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

- Результати виводяться в формі таблиці:
  

|    |   A |   B |   C |   D |
|----|-----|-----|-----|-----|
| A  |   0 |   1 |   3 |   4 |
| B  |   1 |   0 |   2 |   3 |
| C  |   3 |   2 |   0 |   1 |
| D  |   4 |   3 |   1 |   0 |

# Завдання 4. Візуалізація піраміди 
# Завдання 5. Візуалізація обходу бінарного дерева

![task_4_5](https://github.com/IIchukissII/goit-algo-fp/assets/133657307/073f17dd-d813-4be4-8765-129b116a0b29)

В класі реалізовані наступні мктоди:
- **draw_tree("Title")** - Візуалізує бінрну купу
- **bfs_iterative()** - Пошук у ширину (BFS), відвідує всі вершини на певному рівні перед тим, як перейти до наступного рівня
- **dfs_iterative()** - Пошук у глибину (DFS), виконується шляхом відвідування вершини, а потім рекурсивного відвідування всіх сусідніх вершин, які ще не були відвідані. 
- **change_min_heap(True)** - Дає можливість обирати між мініманою (по замовчуванню - False) та максимальною
- **heappop()** - Видаляє і повертає найменший чи найменший вузол купи, в залежності від її виду.
- **heappush(key)** - Додає вузол в купу

# Завдання 6: Жадібні алгоритми та динамічне програмування

Програма, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

# Завдання 7: Використання методу Монте-Карло
Програма, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

![task_7](https://github.com/IIchukissII/goit-algo-fp/assets/133657307/5917f320-f892-4399-87fc-c3448a8304be)


│   Sum │   Probability │
|-------|---------------|
│     2 │        0.0276 │
├───────┼───────────────┤
│     3 │        0.0555 │
├───────┼───────────────┤
│     4 │        0.0837 │
├───────┼───────────────┤
│     5 │        0.1111 │
├───────┼───────────────┤
│     6 │        0.1392 │
├───────┼───────────────┤
│     7 │        0.1662 │
├───────┼───────────────┤
│     8 │        0.1389 │
├───────┼───────────────┤
│     9 │        0.1115 │
├───────┼───────────────┤
│    10 │        0.0830 │
├───────┼───────────────┤
│    11 │        0.0555 │
├───────┼───────────────┤
│    12 │        0.0278 │
╘═══════╧═══════════════╛
