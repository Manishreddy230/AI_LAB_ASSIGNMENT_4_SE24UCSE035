import itertools

letters = ['T', 'W', 'O', 'F', 'U', 'R']
digits = range(10)

for perm in itertools.permutations(digits, len(letters)):
    d = dict(zip(letters, perm))
    
    # Leading digits should not be zero
    if d['T'] == 0 or d['F'] == 0:
        continue
    
    TWO = d['T'] * 100 + d['W'] * 10 + d['O']
    FOUR = d['F'] * 1000 + d['O'] * 100 + d['U'] * 10 + d['R']
    
    if TWO + TWO == FOUR:
        print("Solution:\n")
        print("T =", d['T'])
        print("W =", d['W'])
        print("O =", d['O'])
        print("F =", d['F'])
        print("U =", d['U'])
        print("R =", d['R'])
        
        print("\nVerification:")
        print(TWO, "+", TWO, "=", FOUR)
        break
