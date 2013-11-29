#!/usr/bin/env python

# Terminal and nonterminals.
nil, a, b, A, B, C, S = range(7)
# Their string representation.
variables = { nil: '0',
              a: 'a',
              b: 'b',
              A: 'A',
              B: 'B',
              C: 'C',
              S: 'S' }

productions = {}
def add_production(a,b,c):
    global productions
    try:
        p = productions[a,b]
        p.append(c)
    except KeyError:
        productions[a,b] = [c]

# Grammar in CNF.
add_production(A, B, S)  # S -> AB
add_production(B, C, S)  # S -> BC
add_production(B, A, A)  # A -> BA
add_production(a, nil, A) # A -> a
add_production(C, C, B)   # B -> CC
add_production(b, nil, B) # B -> b
add_production(A, B, C)   # C -> AB
add_production(a, nil, C) # C -> a

# The word to parse.
w = [a,b,a,b,a,a]
L = len(w)

# Parse table.
X = [[set([]) for i in range(L)] for i in range(L)]

# Print the parse table.
def print_table(X):
    for step in range(len(X) - 1, -1, -1):
        for i in range(len(X) - step):
            j = i + step
            print(''.join([variables[v] for v in X[i][j]]), end="\t")
        print()

# Induction base: fill the triangle base from the terminals.
for i in range(L):
    X[i][i] = productions[w[i], nil]

# Return the set of allowed productions of all combinations of AB.
def derive(A, B):
    global productions
    pairs = ((a,b) for a in A for b in B)
    result = set([])
    for a,b in pairs:
        try:
            result |= set(productions[a,b])
        except KeyError:
            pass
    return result

# Induction: fill the parse table bottom-up.
for step in range(1, len(X)):
    for i in range(len(X) - step):
        j = i + step
        for k in range(i, j):
            X[i][j] |= derive(X[i][k], X[k+1][j])

# Print the resulting parse table.
print_table(X)

if __name__ == "__main__":
    pass
