#Best Solution
def f(a,b):
	for i in range(len(a)):
		if b in a[i]:
			return True
		else:
			continue
	return False


# def find_matrix(a,b):
# 	if a==None or a.length==0 or a[0].length==0:
# 		return 0
# 	m=len(a)
# 	n=len(a[0])
# 	start=0
# 	end=m*n-1
# 	while (start<=end):
# 		mid=(start+end)//2
# 		midx=mid//n
# 		midy=mid%n
# 		if (a[midx][midy]==b):
# 			return 1
# 		elif (matrix[midx][midy]<b):
# 			start=mid+1
# 		else:
# 			end=mid-1
# 	return 0

	# if (a==None or len(a)==0 or len(a[0])==0):
 #            return 0
 #        if (len(a)==1 and len(a[0])==1):
 #            if a[0][0]==b:
 #                return 1
 #            else:
 #                return 0
 #        m=len(a)-1
 #        n=len(a[0])-1
 #        start=0
 #        end=m*n-1
 #        while (start<=end):
 #            mid=(start+end)//2
 #            midx=mid//n
 #            midy=mid%n
 #            if (a[midx][midy]==b):
 #                return 1
 #            elif (a[midx][midy]<b):
 #                start=mid+1
 #            else:
 #                end=mid-1
 #        return 0


 #a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
a=[[3, 3, 11, 12, 14],
  [16, 17, 30, 34, 35],
  [45, 48, 49, 50, 52],
  [56, 59, 63, 63, 65],
  [67, 71, 72, 73, 79],
  [80, 84, 85, 85, 88],
  [88, 91, 92, 93, 94]]
print(f(a,int(input())))
