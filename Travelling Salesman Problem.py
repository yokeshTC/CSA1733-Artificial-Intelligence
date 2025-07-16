from itertools import permutations

def travelling_salesman(distance_matrix):
    n = len(distance_matrix)
    cities = range(1, n)
    min_cost = float('inf')
    best_path = []

    for path in permutations(cities):
        current_cost = 0
        current_path = [0] + list(path) + [0]

        for i in range(n):
            current_cost += distance_matrix[current_path[i]][current_path[i + 1]]

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    print("Minimum cost:", min_cost)
    print("Best path:", ' -> '.join(str(city) for city in best_path))

if __name__ == "__main__":
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    travelling_salesman(distance_matrix)
