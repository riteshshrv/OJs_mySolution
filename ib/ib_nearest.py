'''Given an array, find the nearest smaller element G[i] for every element A[i] in the array 
	such that the element has an index smaller than i.

More formally,

G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.'''


def prevSmaller(arr):
        n=len(arr)
        a=[]
        s=[]
        for i in range(n):
            while len(s) != 0 and s[-1]>=arr[i]:
                s.pop()
            if len(s)==0:
                a.append(-1)
            else:
                a.append(s[-1])
            s.append(arr[i])
        return a