def evalRPN(a):
    operators = "+-*/"
    num = "123456789"
    s = []
    for i in a:
        print(i)
        if i in num:
            s.append(int(i))
        elif i in operators:
            t2 = s.pop()
            t1 = s.pop()
            if i == "+":
                s.append(t1+t2)
            elif i == "-":
                s.append(t1-t2)
            elif i == "*":
                s.append(t1*t2)
            elif i == "/":
                s.append(t1/t2)
        else:
            s.append(int(i))
        print s
    g = int(''.join(str(x) for x in s))
    return g   


a = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
b = ["4", "13", "5", "/", "+"]
assert evalRPN(b)