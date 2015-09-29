'''spoj no. of commmon words in two strings.'''

while True:
    s1 = input()
    if s1 == "":
        break
    s2 = input()
    a = list(set(s1).intersection(s2))
    print(len(a))
