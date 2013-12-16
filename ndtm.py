#!/usr/bin/env python3

# Non-deterministic Turing machine from the week 5 homework.

# States
q0 = 'q₀'
q1 = 'q₁'
q2 = 'q₂'
qf = 'qf'

# Direction
L = -1
R = 1

# Blank
B = -1

# Transition function
delta = {
    (q0,0): [(q1,0,R)],
    (q0,1): [(q1,0,R)],
    (q0,B): [(q1,0,R)],
    (q1,0): [(q1,1,R),(q2,0,L)],
    (q1,1): [(q1,1,R),(q2,1,L)],
    (q1,B): [(q1,1,R),(q2,B,L)],
    (q2,0): [(qf,0,R)],
    (q2,1): [(q2,1,L)]
    }

state = set([(0,q0,"1010")])

def print_state(state):
    for (idx,q,tape) in state:
        print("%s%s%s" % (tape[:idx], q, tape[idx:]))

def symb_to_tape(s):
    if s == B:
        return ' '
    return str(s)

def tape_to_symb(c):
    if c == ' ':
        return B
    return int(c)

def next_state(delta, state):
    new_state = set([])
    for (idx,q,tape) in state:
        try:
            c = tape[idx]
            symb = tape_to_symb(tape[idx])
        except IndexError:
            symb = B
        try:
            transition = delta[(q,symb)]
            for (new_q, new_symb, direction) in transition:
                new_tape = tape[:idx] + symb_to_tape(new_symb) + tape[idx+1:]
                new_state.add((idx + direction, new_q, new_tape))
        except KeyError:
            pass
    return new_state

state = next_state(delta, state)
state = next_state(delta, state)
state = next_state(delta, state)
state = next_state(delta, state)
state = next_state(delta, state)
print_state(state)
