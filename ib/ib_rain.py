'''RAINBookmark
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.'''

def trap(self, a):
        if a==None:
            return -1
        n=len(a)
        if n<2:
            return 0
        
        l=[0]*n
        r=[0]*n
        l[0], r[-1]= a[0], a[-1] 
        
        for i in range(1,n):
            l[i]=max(l[i-1],a[i])
            
        for i in range(n-2,-1,-1):
            r[i]=max(r[i+1],a[i])
            
        water=0
        for i in range(n):
            water += min(l[i],r[i])-a[i]
            
        return water
