def searchInsert(self, a, b):
        if len(a)==0 or a==None:
            return -1
        
        return self._my_search(a,b,0,len(a)-1)
    
    def _my_search(self,a,b,low,high):
        mid=(low+high)//2
        if (b==a[mid]):
            return mid
        elif (b<a[mid]):
            return self._my_search(a,b,low,mid-1) if (low<mid) else low
        else:
            return self._my_search(a,b,mid+1,high) if (high>mid) else high+1