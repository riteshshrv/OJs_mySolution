def main():
    for t in range(int(input())):
        a, b = [int(x) for x in input().split()]
        hcf = gcd(a, b)
        lcm = (a*b)/hcf
        print("%g" % hcf, " ", "%i" % lcm)


def gcd(i, j):
    if j == 0:
        return i
    else:
        return (gcd(j, i % j))

if __name__ == "__main__":
    main()
# flake8: noqa
