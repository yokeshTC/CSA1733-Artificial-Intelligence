# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:07:02 2025

@author: DELL
"""

from queue import PriorityQueue

def a_star(graph, start, goal, heuristic):
    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]
    
    while not open_list.empty():
        _, current = open_list.get()
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                open_list.put((f_score[neighbor], neighbor))
    
    return None  # No path found

# Example Graph Representation (Adjacency List)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

# Heuristic values (estimated cost from each node to goal)
heuristic = {
    'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0
}

start_node = 'A'
goal_node = 'E'

path = a_star(graph, start_node, goal_node, heuristic)
print("Shortest Path using A*:", path)