from collections import deque

initial_state = (3, 3, 1)  
goal_state = (0, 0, 0)


moves = [(2, 0), (0, 2), (1, 0), (0, 1), (1, 1)]

def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left


    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False


    if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
        return False

    return True

def bfs():
    queue = deque()
    visited = set()
    parent = {}

    queue.append(initial_state)
    visited.add(initial_state)
    parent[initial_state] = None

    while queue:
        current = queue.popleft()

        if current == goal_state:
            return reconstruct_path(parent, current)

        m, c, boat = current

        direction = -1 if boat == 1 else 1
        for m_move, c_move in moves:
            new_m = m + direction * m_move
            new_c = c + direction * c_move
            new_boat = 1 - boat

            new_state = (new_m, new_c, new_boat)

            if is_valid(new_m, new_c) and new_state not in visited:
                visited.add(new_state)
                parent[new_state] = current
                queue.append(new_state)

    return None  # No solution

def reconstruct_path(parent, state):
    path = []
    while state:
        path.append(state)
        state = parent[state]
    path.reverse()
    return path

def print_solution(path):
    for i, (m, c, boat) in enumerate(path):
        side = 'left' if boat == 1 else 'right'
        print(f"Step {i}: Missionaries: {m}, Cannibals: {c}, Boat on {side} side")

# Run the solution
if __name__ == "__main__":
    solution = bfs()
    if solution:
        print("Solution found:\n")
        print_solution(solution)
    else:
        print("No solution found.")
