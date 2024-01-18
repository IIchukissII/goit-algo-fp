class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sorted(self, other_list):
        merged_list = LinkedList()
        current1 = self.head
        current2 = other_list.head

        if current1 is None:
            return other_list
        if current2 is None:
            return self

        if current1.data <= current2.data:
            merged_list.head = current1
            current1 = current1.next
        else:
            merged_list.head = current2
            current2 = current2.next

        current_merged = merged_list.head

        while current1 and current2:
            if current1.data <= current2.data:
                current_merged.next = current1
                current1 = current1.next
            else:
                current_merged.next = current2
                current2 = current2.next
            current_merged = current_merged.next

        if current1:
            current_merged.next = current1
        else:
            current_merged.next = current2

        return merged_list

    def insertion_sort(self):
        sorted_list = LinkedList()
        current = self.head

        while current:
            next_node = current.next
            sorted_list.insert_sorted(current)
            current = next_node

        self.head = sorted_list.head

    def insert_sorted(self, new_node):
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Приклад використання

# Створення однозв'язного списку
linked_list = LinkedList()
node1 = Node(1)
node2 = Node(3)
node3 = Node(2)
linked_list.head = node1
node1.next = node2
node2.next = node3

# Виведення початкового списку
print("Початковий список:")
linked_list.display()

# Реверсування списку
linked_list.reverse()
print("Реверсований список:")
linked_list.display()

# Створення другого однозв'язного списку
other_linked_list = LinkedList()
other_node1 = Node(5)
other_node2 = Node(4)
other_linked_list.head = other_node1
other_node1.next = other_node2

# Об'єднання двох відсортованих списків
merged_list = linked_list.merge_sorted(other_linked_list)
print("Об'єднаний список:")
merged_list.display()

# Сортування однозв'язного списку
linked_list.insertion_sort()
print("Відсортований список:")
linked_list.display()
