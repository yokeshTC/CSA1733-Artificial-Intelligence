from itertools import permutations

def solve_cryptarithmetic():
    letters = 'SENDMORY'
    
    for perm in permutations(range(10), len(letters)):
        s, e, n, d, m, o, r, y = perm

        if s == 0 or m == 0:
            continue

        send = s*1000 + e*100 + n*10 + d
        more = m*1000 + o*100 + r*10 + e
        money = m*10000 + o*1000 + n*100 + e*10 + y


        if send + more == money:
            print("Solution Found:")
            print(f" SEND = {send}")
            print(f"+MORE = {more}")
            print(f"-----")
            print(f"MONEY = {money}")
            print("\nLetter to Digit Mapping:")
            print(dict(zip(letters, perm)))
            return

    print("No solution found.")

if __name__ == "__main__":
    solve_cryptarithmetic()
