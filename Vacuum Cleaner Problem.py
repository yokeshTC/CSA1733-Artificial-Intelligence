def vacuum_cleaner_problem(start_room, status):
    actions = []
    current_room = start_room

    print("Initial State: Room A -", status['A'], ", Room B -", status['B'])
    print("Vacuum starts in Room", current_room)

    if status[current_room] == 'dirty':
        actions.append("Clean Room " + current_room)
        status[current_room] = 'clean'

    other_room = 'B' if current_room == 'A' else 'A'
    actions.append("Move to Room " + other_room)

    if status[other_room] == 'dirty':
        actions.append("Clean Room " + other_room)
        status[other_room] = 'clean'

    print()
    print("Actions taken:")
    for act in actions:
        print("-", act)

    print()
    print("Final State: Room A -", status['A'], ", Room B -", status['B'])

if __name__ == "__main__":
    initial_status = {
        'A': 'dirty',
        'B': 'dirty'
    }
    start_room = 'A'
    vacuum_cleaner_problem(start_room, initial_status)
