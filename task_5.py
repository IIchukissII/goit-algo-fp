import heapq
import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class BinaryTreeNode:

    def __init__(self, key=None, color="lightblue"):
        self.key = key
        self.color = color
        self.id = str(uuid.uuid4())
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root=None):
        self.root = root

    @staticmethod
    def heap_sort(iterable, descending=False):
        sign = -1 if descending else 1
        h = [sign * el for el in iterable]
        heapq.heapify(h)
        return [sign * heapq.heappop(h) for _ in range(len(h))]

    def insert_node(self, heap, index=0):
        if not heap:
            return None

        root = BinaryTreeNode(heap[index])

        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(heap):
            root.left = self.insert_node(heap, left_index)

        if right_index < len(heap):
            root.right = self.insert_node(heap, right_index)

        return root

    def draw_tree(self):
        if self.root is not None:
            G = nx.Graph()
            pos_data = self._draw_tree(G, self.root, 0, 0, 1, 0.5)

            # Extract node positions and colors
            pos = {node: data['pos'] for node, data in pos_data.items()}
            node_colors = [data['color'] for _, data in pos_data.items()]

            labels = {node: str(node.key) for node in G.nodes}

            nx.draw(G, pos, labels=labels, with_labels=True, font_size=8,
                    node_size=2500, node_color=node_colors, font_weight='bold')
            plt.show()

    def _draw_tree(self, G, node, x, y, level, dx):
        if node is not None:
            G.add_node(node, pos=(x, y), color=node.color)  # Include color attribute
            if node.left is not None:
                G.add_edge(node, node.left)
                x_left = x - dx / level
                y_left = y - 1
                self._draw_tree(G, node.left, x_left, y_left, level * 2, dx)
            if node.right is not None:
                G.add_edge(node, node.right)
                x_right = x + dx / level
                y_right = y - 1
                self._draw_tree(G, node.right, x_right, y_right, level * 2, dx)
        return {n: {'pos': data['pos'], 'color': data['color']} for n, data in G.nodes(data=True)}

    def dfs_iterative(self, base_color=(0.06, 1.00, 0.70), lightening_factor=0.8):
        if self.root is not None:
            stack = [self.root]
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
        if not self.root:
            return

        visited = set()
        queue = deque([self.root])

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

    def push(self, key):
        heap = self.heap_sort(self.in_order_traversal())
        heap.append(key)
        self.root = self.insert_node(heap)

    def pop(self):
        heap = self.heap_sort(self.in_order_traversal())
        heap.pop()
        self.root = self.insert_node(heap)

    def in_order_traversal(self):
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.key)
                traverse(node.right)

        traverse(self.root)
        return result


def main():
    unsorted_list = [20, 30, 25, 19, 27, -1, -2, 18, 22, 10, 11, 12, 13]

    tree = BinaryTree(BinaryTreeNode(unsorted_list[0]))
    tree.root = tree.insert_node(unsorted_list)

    tree.dfs_iterative()
    tree.draw_tree()

    tree.bfs_iterative()
    tree.draw_tree()

    # Push and Pop operations
    tree.push(5)
    tree.dfs_iterative()
    tree.draw_tree()

    tree.pop()
    tree.dfs_iterative()
    tree.draw_tree()


if __name__ == "__main__":
    main()
