'''The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.'''

class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, n):
        if n == 0 :
            return ""
        actual =['1']
        for i in range(1,n):
            previous = actual
            actual = []
            actChar = previous[0]
            count = 1
            for j in range(1, len(previous)):
                if previous[j] == actChar:
                    count += 1
                else:
                    actual.append(str(count))
                    actual.append(actChar)
                    actChar = previous[j]
                    count = 1
            actual.append(str(count))
            actual.append(actChar)
        return ''.join(actual)
