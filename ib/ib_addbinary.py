'''Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"
Return a + b = “111”.'''

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, a, b):
        a=int(a,2)
        b=int(b,2)
        sum=a+b
        return format(sum,'b')
