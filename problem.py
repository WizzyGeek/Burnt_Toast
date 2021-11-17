def flip(n, array):
    sub = array[:n]
    for i in sub:
        i[1] = not i[1]
    sub.reverse()
    array[:n] = sub


def problem(x, debug=False):
    array = [[i, True] for i in range(x)]

    itr = 0
    n = 1
    while True:
        itr +=1
        flip(n, array)
        if debug:
            print(" | ".join(("↓", "↑")[i[1]] + f"({i[0]})" for i in array), itr, n)
        if all(i[1] for i in array):
            to_ret = True
            for idx, i in enumerate(array):
                if idx != i[0]:
                    to_ret = False
                    break
            if to_ret:
                return itr

        n = (n % x) + 1

def main():
    import sys

    if sys.argv[1:]:
        if "th" in sys.argv:
            with open("ret.txt", "w") as ret:
                done = 1
                for i in range(2, 1000):
                    ret.write(str(i) + " " + str(problem(i)) + "\n")
                    print("")
        else:
            print(problem(int(sys.argv[1]), debug=True))
    else:
        try:
            i = 2
            while True:
                print(i, problem(i))
                i += 1
        except KeyboardInterrupt:
            print("Exit.")

main()
