'''Design a stack that supports push, pop, top, and retrieving the 
minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.'''

class MinStack:
    
    def __init__(self):
        self.d=[]
        self.m=[]
        self.mv=-1
    
    # @param x, an integer
    def push(self, x):
        if len(self.d)==0:
            self.m.append(x)
            self.mv=x
        self.d.append(x)
        if x<self.mv:
            self.mv=x
            self.m.append(x)

    # @return nothing
    def pop(self):
        try:
            p=self.d.pop()
            if p==self.m[-1]:
                self.m.remove(p)
                self.mv=self.m[-1]
        except:
            pass
    
    # @return an integer
    def top(self):
        if len(self.d)==0:
            return -1
        return self.d[-1]

    # @return an integer
    def getMin(self):
        if len(self.m)==0:
            return -1
        return self.mv

