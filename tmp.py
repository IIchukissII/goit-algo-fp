import heapq
import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from functools import total_ordering


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
        return self.key < other.key

    def __hash__(self):
        return hash(self.id)


class HeapTree:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.heap = []
        self.node = BinaryTreeNode()

    def __hash__(self):
        return hash(self.id)

    def heapify(self):
        heapq.heapify(self.heap)

    def heappop(self):
        return heapq.heappop(self.heap)

    def heappush(self, node):
        heapq.heappush(self.heap, (node.key, node))

    def insert_from_heap(self, heap, index=0):
        if not heap:
            return None

        root = BinaryTreeNode(heap[index])
        self.heap.append(root)  # Add root to the heap

        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(heap):
            if not self.node.left:
                self.node.left = BinaryTreeNode(heap[index])
            self.node.left.insert_node(heap, left_index)

        if right_index < len(heap):
            if not self.node.right:
                self.node.right = BinaryTreeNode(heap[index])
            self.node.right.insert_node(heap, right_index)

        return self

    def draw_tree(self, title="Binary Tree"):
        if self.heap:
            G = nx.Graph()
            pos_data = self._draw_tree(G, 0, 0, 0, 1, 0.5)  # Pass dx as 0.5

            pos = {node: data['pos'] for node, data in pos_data.items()}
            node_colors = [data['color'] for _, data in pos_data.items()]
            labels = {node: str(node.key) for node in G.nodes}

            nx.draw(G, pos, labels=labels, with_labels=True, font_size=8,
                    node_size=2500, node_color=node_colors, font_weight='bold')
            plt.title(title)
            plt.show()

    def _draw_tree(self, G, index, x, y, level, dx):
        if index < len(self.heap):
            node = self.heap[index]
            G.add_node(node, pos=(x, y), color=node.color)
            if node.left is not None:
                left_index = 2 * index + 1
                G.add_edge(node, self.heap[left_index])
                x_left = x - dx / level
                y_left = y - 1
                self._draw_tree(G, left_index, x_left, y_left, level * 2, dx)
            if node.right is not None:
                right_index = 2 * index + 2
                G.add_edge(node, self.heap[right_index])
                x_right = x + dx / level
                y_right = y - 1
                self._draw_tree(G, right_index, x_right, y_right, level * 2, dx)
        return {n: {'pos': data['pos'], 'color': data['color']} for n, data in G.nodes(data=True)}

    def dfs_iterative(self, base_color=(0.06, 1.00, 0.70), lightening_factor=0.8):
        if self.heap:
            stack = [self.heap[0]]
            visited = set()

            while stack:
                current_node = stack.pop()
                if current_node not in visited:
                    current_node.color = base_color
                    base_color = tuple(c ** lightening_factor for c in base_color)
                    visited.add(current_node)

                    if current_node.right:
                        stack.append(current_node.right)

                    if current_node.left:
                        stack.append(current_node.left)

    def bfs_iterative(self, base_color=(0.06, 1.00, 0.70), lightening_factor=0.8):
        if self.heap:
            visited = set()
            queue = deque([self.heap[0]])

            while queue:
                node = queue.popleft()
                if node not in visited:
                    node.color = base_color
                    base_color = tuple(c ** lightening_factor for c in base_color)
                    visited.add(node)

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)


def main():
    # Create a binary tree from an unsorted list
    unsorted_list = [20, 30, 25, 19, 27, -1, -2, 18, 22, 10, 11, 12, 13]
    tree = HeapTree()
    tree.insert_from_heap(unsorted_list)

    # Visualize the original tree
    tree.dfs_iterative()
    tree.draw_tree("Original Tree")

    # Perform heap operations
    tree.heapify()
    popped_node = tree.heappop()
    new_node = BinaryTreeNode(56)
    tree.heappush(new_node)

    # Visualize the tree after heap operations
    tree.dfs_iterative()
    tree.draw_tree("After Heap Operations")


if __name__ == "__main__":
    main()
