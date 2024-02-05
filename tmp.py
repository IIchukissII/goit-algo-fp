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
        return self.key == other.key

    def __hash__(self):
        return hash(self.id)

    def _insert_from_heap(self, heap, index=0):
        if not heap:
            return None

        self.key = heap[index]

        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(heap):
            if not self.left:
                self.left = BinaryTreeNode(heap[left_index])
            self.left._insert_from_heap(heap, left_index)

        if right_index < len(heap):
            if not self.right:
                self.right = BinaryTreeNode(heap[right_index])
            self.right._insert_from_heap(heap, right_index)

        return self

    def find_node(self, id):
        if self.id == id:
            return self
        if self.left and self.left.id == id:
            return self.left
        if self.right and self.right.id == id:
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
        return {n: {'pos': data['pos'], 'color': data['color']} for n, data in G.nodes(data=True)}

    def _dfs_iterative(self, base_color=(0.06, 1.00, 0.70), lightening_factor=0.8):
        stack = [self.find_node(self.id)]
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

    def _bfs_iterative(self, base_color=(0.06, 1.00, 0.70), lightening_factor=0.8):
        visited = set()
        queue = deque([self.find_node(self.id)])

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

    def insert_from_heap(self, heap=None, index=0):
        if not self.heap:
            heapq.heapify(heap)
            self.heap = heap
        else:
            heapq.heapify(self.heap)
            heap = self.heap
        return self.node._insert_from_heap(heap, index)

    def draw_tree(self, title="Binary Tree"):
        if self.node is not None:
            G = nx.Graph()
            pos_data = self.node._draw_tree(G, 0, 0, 1, 0.5)  # Pass dx as 0.5

            pos = {node: data['pos'] for node, data in pos_data.items()}
            node_colors = [data['color'] for _, data in pos_data.items()]
            labels = {node: str(node.key) for node in G.nodes}

            nx.draw(G, pos, labels=labels, with_labels=True, font_size=8,
                    node_size=2500, node_color=node_colors, font_weight='bold')
            plt.title(title)
            plt.show()

    def dfs_iterative(self, base_color=(0.06, 1.00, 0.70), lightening_factor=0.8):
        return self.node._dfs_iterative(base_color, lightening_factor)

    def bfs_iterative(self, base_color=(0.06, 1.00, 0.70), lightening_factor=0.8):
        return self.node._bfs_iterative(base_color, lightening_factor)


def main():
    # Create a binary tree from an unsorted list
    unsorted_list = [20, 30, 25, 19, 27, -1, -2, 18, 22, 10, 11, 12, 13]
    tree = HeapTree()
    tree.insert_from_heap(unsorted_list)

    # Visualize the original tree
    tree.dfs_iterative()
    tree.draw_tree("Original Tree")

    tree.bfs_iterative()
    tree.draw_tree("Original Tree")

    print(tree.heappop())
    tree.insert_from_heap()
    tree.draw_tree("Original Tree")

if __name__ == "__main__":
    main()
