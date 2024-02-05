import heapq
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def print_shortest_paths_table(graph):
    vertices = list(graph.keys())
    table_data = {vertex: dijkstra(graph, vertex) for vertex in vertices}

    df = pd.DataFrame(table_data)
    df.index = vertices

    print("Table of shortest paths:")
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

    return df


def visualize_graph(graph):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)

    weights = {}

    for node1, neighbors in graph.items():
        for node2, weight in neighbors.items():
            if (node2, node1) not in weights:
                weights[(node1, node2)] = weight
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

    plt.show()


def main():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    print_shortest_paths_table(graph)
    visualize_graph(graph)


if __name__ == '__main__':
    main()
