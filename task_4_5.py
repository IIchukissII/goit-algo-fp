import heapq
import uuid
from collections import deque
from functools import total_ordering

import matplotlib.pyplot as plt
import networkx as nx


@total_ordering
class BinaryTreeNode:
    def __init__(self, key=None, color="lightblue"):
        self.key = key
        self.color = color
        self.id = str(uuid.uuid4())
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.key < other.key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.id)

    def remove_all_children(self):
        if self.left:
            self.left.remove_all_children()
            self.left = None
        if self.right:
            self.right.remove_all_children()
            self.right = None

    def _insert_from_heap(self, heap, index=0):
        if index == 0:
            self.remove_all_children()
        if not heap:
            return None

        self.key = heap[index].key

        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(heap):
            if not self.left:
                self.left = heap[left_index]
            self.left._insert_from_heap(heap, left_index)

        if right_index < len(heap):
            if not self.right:
                self.right = heap[right_index]
            self.right._insert_from_heap(heap, right_index)

        return self

    def find_node(self, node_id):
        if self.id == node_id:
            return self
        if self.left and self.left.id == node_id:
            return self.left
        if self.right and self.right.id == node_id:
            return self.right
        return None

    def _draw_tree(self, G, x, y, level, dx):
        if self is not None:
            G.add_node(self, pos=(x, y), color=self.color)  # Include color attribute
            if self.left is not None:
                G.add_edge(self, self.left)
                x_left = x - dx / level
                y_left = y - 1
                self.left._draw_tree(G, x_left, y_left, level * 2, dx)
            if self.right is not None:
                G.add_edge(self, self.right)
                x_right = x + dx / level
                y_right = y - 1
                self.right._draw_tree(G, x_right, y_right, level * 2, dx)
        return {
            n: {"pos": data["pos"], "color": data["color"]}
            for n, data in G.nodes(data=True)
        }

    def _dfs_iterative(self, base_color=(0.06, 1.00, 0.70), lightening_factor=0.8):
        stack = [self.find_node(self.id)]
        visited = set()

        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                current_node.color = base_color
                base_color = tuple(c**lightening_factor for c in base_color)
                visited.add(current_node)

                if current_node.right:
                    stack.append(current_node.right)

                if current_node.left:
                    stack.append(current_node.left)

    def _bfs_iterative(self, base_color=(0.06, 1.00, 0.70), lightening_factor=0.8):
        visited = set()
        queue = deque([self.find_node(self.id)])

        while queue:
            node = queue.popleft()
            if node not in visited:
                node.color = base_color
                base_color = tuple(c**lightening_factor for c in base_color)
                visited.add(node)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)


class HeapTree:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.heap = []
        self.node = BinaryTreeNode()
        self.min_heap = False

    def __hash__(self):
        return hash(self.id)

    def change_min_heap(self, min_flag):
        self.min_heap = min_flag
        self.heap_sort()

    def heapify(self):
        heapq.heapify(self.heap)

    def heap_sort(self):
        sign = -1 if self.min_heap else 1
        for el in self.heap:
            el.key = sign * el.key
        self.heapify()
        for el in self.heap:
            el.key = sign * el.key
        self.insert_from_heap()

    def heappop(self):
        pop_node = heapq.heappop(self.heap)
        self.heap_sort()
        self.insert_from_heap()
        return pop_node

    def heappush(self, key):
        heapq.heappush(self.heap, BinaryTreeNode(key))
        self.heap_sort()
        self.insert_from_heap()

    def insert_from_heap(self, heap=None, index=0):
        if not self.heap:
            if not self.min_heap:
                heapq.heapify(heap)
            self.heap = [BinaryTreeNode(el) for el in heap]
            heap = self.heap
        else:
            if not self.min_heap:
                self.heap_sort()
            heap = self.heap
        return self.node._insert_from_heap(heap, index)

    def draw_tree(self, title="Binary Tree"):
        if self.node is not None:
            G = nx.Graph()
            G.name = title
            pos_data = self.node._draw_tree(G, 0, 0, 1, 0.5)  # Pass dx as 0.5

            pos = {node: data["pos"] for node, data in pos_data.items()}
            node_colors = [data["color"] for _, data in pos_data.items()]
            labels = {node: str(node.key) for node in G.nodes}

            nx.draw(
                G,
                pos,
                labels=labels,
                with_labels=True,
                font_size=8,
                node_size=2500,
                node_color=node_colors,
                font_weight="bold",
            )
            plt.suptitle(title, x=0.1, y=0.9)  # Set the y parameter to adjust the position of the title
            plt.show()

    def dfs_iterative(self, base_color=(0.06, 1.00, 0.70), lightening_factor=0.8):
        return self.node._dfs_iterative(base_color, lightening_factor)

    def bfs_iterative(self, base_color=(0.06, 1.00, 0.70), lightening_factor=0.8):
        return self.node._bfs_iterative(base_color, lightening_factor)


def main():
    unsorted_list = [20, 30, 25, 19, 27, -1, -2, 18, 22, 10, 11, 12, 13]
    tree = HeapTree()
    tree.insert_from_heap(unsorted_list)
    tree.draw_tree("Original Tree")

    tree.bfs_iterative()
    tree.draw_tree("BFS")

    tree.change_min_heap(True)
    tree.dfs_iterative()
    tree.draw_tree("DFS max heap")

    node_pop = tree.heappop()
    tree.bfs_iterative()
    tree.draw_tree(f"After pop {node_pop.key}")

    tree.heappush(35)
    tree.bfs_iterative()
    tree.draw_tree(f"After push {35}")


if __name__ == "__main__":
    main()
