#!/usr/bin/env python

# Simulate push-down automaton (PDA)

# States
p = 'p'
q = 'q'

# Epsylon for the input
eps = 'ε'

# Stack symbols
Z0 = 'Z0'
X = 'X'

# Transition function
delta = {
    (q,0,Z0): (q,[X,Z0]),
    (q,0,X): (q,[X,X]),
    (q,1,X): (q,[X]),
    (q,eps,X): (p,[]),
    (p,eps,X): (p,[]),
    (p,1,X): (p,[X,X]),
    (p,1,Z0): (p,[])
    }

# Initial set of states
state = (q,[Z0])

def print_state(s):
    state, stack = s
    print(state, "".join(reversed(stack)))

print_state(state)

# Calculate set of states after consuming a symbol.
def process(state, symbol):
    (s, st) = state
    try:
        new_s, new_st = delta[s, symbol, st.pop()]
        for new_push in reversed(new_st):
            st.append(new_push)
        if st:
            return (new_s, st)
    except KeyError:
        pass
    except IndexError:
        pass

#task = (1,1,1,0,0,1)
#task = (0,1,0,1,0,1,0)
#task = (0,0,1,1,1,0,0)
task = (0,1,1,0,1,1,0,1,1)
for symb in task:
    state = process(state, symb)
    print_state(state)
print("---")
while True:
    state = process(state, eps)
    print_state(state)
