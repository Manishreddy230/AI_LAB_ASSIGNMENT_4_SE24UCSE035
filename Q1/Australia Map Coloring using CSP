states = ['WA','NT','SA','Q','NSW','V','T']

neighbors = {
    'WA':['NT','SA'],
    'NT':['WA','SA','Q'],
    'SA':['WA','NT','Q','NSW','V'],
    'Q':['NT','SA','NSW'],
    'NSW':['Q','SA','V'],
    'V':['SA','NSW'],
    'T':[]
}

colors = ['Red','Green','Blue']

def is_valid(state, color, assignment):
    for n in neighbors[state]:
        if n in assignment and assignment[n] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(states):
        return assignment

    for s in states:
        if s not in assignment:
            break

    for c in colors:
        if is_valid(s, c, assignment):
            assignment[s] = c
            result = backtrack(assignment)
            if result:
                return result
            del assignment[s]

    return None

solution = backtrack({})

print("Australia Map Coloring:\n")
for s in solution:
    print(s, "->", solution[s])
