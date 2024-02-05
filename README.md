# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком
- Релізовано реверсування однозв'язного списку, змінюючи посилання між вузлами
- Реалізовано алгоритм сортування для однозв'язного списку
- Реалізовано об'єднання двох відсортованих однозв'язних списків в один відсортований список.

# Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії
- Програма візуалізує фрактал “дерево Піфагора”, і користувач має можливість вказати рівень рекурсії.
  Викликається з консолі (приклад виклику - python task_2.py -d *рівень,рекурсії*)
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
  
+----+-----+-----+-----+-----+
|    |   A |   B |   C |   D |
|----+-----+-----+-----+-----|
| A  |   0 |   1 |   3 |   4 |
| B  |   1 |   0 |   2 |   3 |
| C  |   3 |   2 |   0 |   1 |
| D  |   4 |   3 |   1 |   0 |
+----+-----+-----+-----+-----+


