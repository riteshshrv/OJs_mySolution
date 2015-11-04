def maxset(n):
    csum,msum=0,0
    msum_range1=[]
    msum_range=[]
    for i in range(len(n)):
        if n[i]>0:
            csum+=n[i]
            if csum>msum:
                msum=csum
                msum_range1.append(n[i])
        else:
            csum=0
            msum_range.append(msum_range1)
            
    return msum_range

mset=maxset([1, 2, 5, -7, 2, 3])
print(mset)

