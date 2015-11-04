'''HackerEarth Stacks and Queues: Monk's Love for Food '''
s = []
for t in range(int(input())):
    m = [int(x) for x in input().split()]
    if len(m) == 1:
        if m[0] == 1:
            try:
                print(s.pop())
            except IndexError:
                print("No Food")
        else:
            print("error")
    elif len(m) == 2:
        if m[0] == 2:
            s.append(m[1])
        else:
            print("error")
    else:
        print("error")
