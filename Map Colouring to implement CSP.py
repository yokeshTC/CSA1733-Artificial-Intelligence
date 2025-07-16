def is_valid(state, region, color, neighbors):
    for neighbor in neighbors[region]:
        if neighbor in state and state[neighbor] == color:
            return False
    return True

def backtrack(state, regions, colors, neighbors):
    if len(state) == len(regions):
        return state

    unassigned = [r for r in regions if r not in state]
    region = unassigned[0]

    for color in colors:
        if is_valid(state, region, color, neighbors):
            state[region] = color
            result = backtrack(state, regions, colors, neighbors)
            if result:
                return result
            del state[region]

    return None

def map_coloring():
    regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    colors = ['Red', 'Green', 'Blue']
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    result = backtrack({}, regions, colors, neighbors)

    if result:
        for region in regions:
            print(region, "->", result[region])
    else:
        print("No solution found")

if __name__ == "__main__":
    map_coloring()
