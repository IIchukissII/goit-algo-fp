import heapq
import uuid
import networkx as nx
import matplotlib.pyplot as plt


class BinaryHeapNode:
    def __init__(self, key=None, color="lightblue"):
        self.key = key
        self.color = color
        self.id = str(uuid.uuid4())
        self.left = None
        self.right = None
        self.heap = None

    @staticmethod
    def heap_sort(iterable, descending=False):
        sign = -1 if descending else 1
        h = [sign * el for el in iterable]
        heapq.heapify(h)
        return [sign * heapq.heappop(h) for _ in range(len(h))]

    def insert_node(self, heap, index=0):
        if not heap:
            return None

        self.key = heap[index]

        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(heap):
            if not self.left:
                self.left = BinaryHeapNode()
            self.left.insert_node(heap, left_index)

        if right_index < len(heap):
            if not self.right:
                self.right = BinaryHeapNode()
            self.right.insert_node(heap, right_index)

        return self

    def sum_all_nodes(self):
        total = self.key
        if self.left:
            total += self.left.sum_all_nodes()
        if self.right:
            total += self.right.sum_all_nodes()
        return total

    def draw_tree(self):
        G = nx.Graph()
        pos_data = self._draw_tree(G, 0, 0, 1, 0.1)

        # Extract node positions and colors
        pos = {node: data['pos'] for node, data in pos_data.items()}
        node_colors = [data['color'] for _, data in pos_data.items()]

        labels = {node: str(node.key) for node in G.nodes}

        nx.draw(G, pos, labels=labels, with_labels=True, font_size=8,
                node_size=700, node_color=node_colors, font_weight='bold')
        plt.show()

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

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def main():
    # Example usage of heap_sort
    unsorted_list = [20, 30, 25, 19, 27, -1, -2, 18]
    sorted_list_ascending = BinaryHeapNode.heap_sort(unsorted_list)
    root = BinaryHeapNode(sorted_list_ascending[0])
    root.insert_node(sorted_list_ascending)
    print(root)
    sorted_list_descending = BinaryHeapNode.heap_sort(unsorted_list, descending=True)

    print("Original List:", unsorted_list)
    print("Sorted List (Ascending):", sorted_list_ascending)
    print("Sorted List (Descending):", sorted_list_descending)
    # Draw the tree
    root.draw_tree()


if __name__ == "__main__":
    main()
