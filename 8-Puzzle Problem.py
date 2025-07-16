import heapq
GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]
MOVES = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1)
}
def find_position(state, value):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return i, j
    return None

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_i, goal_j = (val - 1) // 3, (val - 1) % 3
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance
def is_goal(state):
    return state == GOAL_STATE
def generate_children(state):
    i, j = find_position(state, 0)
    children = []
    for move, (di, dj) in MOVES.items():
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            children.append((new_state, move))
    return children
def a_star(start_state):
    visited = set()
    heap = []
    heapq.heappush(heap, (manhattan_distance(start_state), 0, start_state, []))

    while heap:
        f, cost, current_state, path = heapq.heappop(heap)

        state_tuple = tuple(tuple(row) for row in current_state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if is_goal(current_state):
            return path + [current_state]

        for child, move in generate_children(current_state):
            new_cost_
