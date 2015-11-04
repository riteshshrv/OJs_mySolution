'''Given an absolute path for a file (Unix-style), simplify it.

Examples:

path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Note that absolute path always begin with ‘/’ ( root directory )
Path will not have whitespace characters.'''

def simplifyPath(a):
        a=a.split('/')
        stack=[]
        for i in a:
            if i=="":
                continue
            elif i==".":
                continue
            elif i=="..":
                if len(stack) != 0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)
        ans="/"+"/".join(stack)
        return ans