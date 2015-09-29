'''HackerEarth Stacks and Queues: Monk and Power of Time'''
from collections import deque
count=0
l=int(input())
call=deque((input().split()),l)
ideal=deque((input().split()),l)
if len(call) != len(ideal):
    print("error")
while len(call) != 0:
    while call[0] != ideal[0]:
        call.append(call.popleft())
        count+=1
    call.popleft()
    ideal.popleft()
    count+=1
print(count)