from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque()
    path = []

    queue.append((0, 0, []))

    while queue:
        a, b, steps = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        steps = steps + [f"Jug1: {a}L, Jug2: {b}L"]

        if a == target or b == target:
            print("Solution path:")
            for step in steps:
                print(step)
            return
        next_states = [
            (jug1, b),          
            (a, jug2),      
            (0, b),             
            (a, 0),             
            (min(a + b, jug1), b - (min(a + b, jug1) - a)),  
            (a - (min(a + b, jug2) - b), min(a + b, jug2))  
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], steps))

    print("No solution found.")

if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target_amount = 2

    water_jug_bfs(jug1_capacity, jug2_capacity, target_amount)
