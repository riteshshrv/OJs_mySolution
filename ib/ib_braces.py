'''Write a program to validate if the input string has redundant braces?
Return 0/1 
 0 -> NO 1 -> YES 

Input will be always a valid expression

and operators allowed are only + , * , - , /

Example:

((a+b)) has redundant braces so answer will be 1
(a + (a + b)) doesn't have have any redundant braces so answer will be 0'''

def braces(A):
        if A==None:
            return -1
        elif len(A)==1:
            return 0
        braces = 0
        for char in A :
            if char == '(' :
                braces += 1
            elif char in "*/+-" :
                braces -= 1
            if braces < 0 :
                braces = 0
        if braces == 0 :
            return 0
        else :
            return 1