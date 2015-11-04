'''HISTOGRAMBookmark
Given n non-negative integers representing the histogram’s bar height where the 
width of each bar is 1, find the area of largest rectangle in the histogram.'''

def largestRectangleArea(height):
        if height==None:
        	return -1
        stack = []
        i = 0
        maxArea = 0
        h = height + [0]
        h_length = len(h)
        while i < h_length:
            # not stack means stack is empty
            if (not stack) or h[stack[-1]] <= h[i]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                maxArea = max(maxArea, h[t] * (i if not stack else i - stack[-1] - 1))
        return maxArea