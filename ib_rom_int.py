# def rom2int(rom):
#     val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     string = rom
#     string = string.upper()
#     total = 0
#     while string:
#         if len(string) == 1 or val[string[0]] >= val[string[1]]:
#             total += val[string[0]]
#             string = string[1:]
#         else:
#             total += val[string[1]] - val[string[0]]
#             string = string[2:]
#     print (total)

# rom2int(input())

def int_to_roman (integer):
    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    parts = []
    for letter, value in table:
        while value <= integer:
            integer -= value
            parts.append(letter)
    return ''.join(parts)

# def rom_to_int(string):
#     table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
#     result = 0
#     string=string.upper()
#     for letter, value in table:
#         while string.startswith(letter):
#             result += value
#             string = string[len(pairs[0]):]
#     return result

def rom_to_int(s):
        numerals = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        sum=0
        s=s[::-1].upper()
        last=None
        for x in s:
            if last and numerals[x]<last:
                sum-=2*numerals[x]
            sum+=numerals[x]
            last=numerals[x]
        return sum

print(int_to_roman(int(input())))
print("\n",rom_to_int(input()))