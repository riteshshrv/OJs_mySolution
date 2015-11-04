# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, a):
        if a==None:
            return -1
        if a.next==None:
            return a
            
        curr=a
        c=0
        # s=[]
        while curr != None:
          c+=1
          # s.append(curr.val)
          curr=curr.next
        
        curr=a
        s=[None]*c
        for i in range(c):
            s[i]=curr.val
            curr=curr.next
        # print(s)
        
        mid=c//2

        self=ListNode(0)
        head=self
        self.next=head
        for i in range(len(s)):
            if i<mid:
                head.next=ListNode(s[-1-i]-s[i])
            else:
                head.next=ListNode(s[i])
            head=head.next
            
        return self.next
                

'''input:  [ 95 -> 59 -> 26 -> 16 -> 31 -> 39 -> 29 -> 8 -> 
  74 -> 14 -> 41 -> 41 -> 64 -> 88 -> 34 -> 21 -> 67 -> 23 
  -> 17 -> 41 -> 3 -> 38 -> 4 -> 45 -> 93 -> 92 -> 99 -> 24 ]

  output: [71, 40, 66, 77, 14, 35, 9, 5, 33, 3, 18, 26, 43, 
  54,3 4, 21, 67, 23, 17, 41, 3, 38, 4, 45, 93, 92, 99, 24]'''

  # class Solution:
  #   def subtract(self, a):
  #       if a==None:
  #           return -1
  #       curr=a
  #       c=0
  #       s=[]
  #       while curr != None:
  #         c+=1
  #         s.append(curr.val)
  #         curr=curr.next
  #       mid=int(c//2)
        
  #       q=[]
  #       for i in range(0,mid):
  #           q.append(s[-1-i]-s[i])
        
  #       for i in range(mid,len(s)):
  #           q.append(s[i])
            
  #       temp=ListNode(self)
  #       temp.val=q[0]
  #       temp.next=None
  #       g=temp
  #       for i in range(1,len(q)):
  #           temp=ListNode(self)
  #           temp.val=q[i]
  #           temp.next=None
  #           temp1=g
  #           while temp1.next != None:
  #               temp1=temp1.next
  #           temp1.next=temp
  #       return g


# class Solution:
#     def subtract(self, a):
#         if a==None:
#             return -1
#         if a.next==None:
#             return a
            
#         curr=a
#         c=0
#         s=[]
#         while curr != None:
#           c+=1
#           s.append(curr.val)
#           curr=curr.next
        
#         mid=c//2

#         temp=ListNode(self)
#         temp.val=(s[-1]-s[0])
#         temp.next=None
#         g=temp
        
#         for i in range(1,len(s)):
#             temp=ListNode(self)
#             if i<mid:
#                 temp.val=(s[-1-i]-s[i])
#             else:
#                 temp.val=s[i]
#             temp.next=None
#             temp1=g
#             while temp1.next != None:
#                 temp1=temp1.next
#             temp1.next=temp
            
#         return g


# class Solution:
#     def subtract(self, a):
#         if a==None:
#             return -1
#         if a.next==None:
#             return a
            
#         curr=a
#         c=0
#         # s=[]
#         while curr != None:
#           c+=1
#           # s.append(curr.val)
#           curr=curr.next
        
#         curr=a
#         s=[None]*c
#         for i in range(c):
#             s[i]=curr.val
#             curr=curr.next
#         # print(s)
        
#         mid=c//2

#         temp=ListNode(s[-1]-s[0])
#         g=temp
        
#         for i in range(1,len(s)):
#             if i<mid:
#                 temp=ListNode(s[-1-i]-s[i])
#             else:
#                 temp=ListNode(s[i])
#             temp1=g
#             while temp1.next:
#                 temp1=temp1.next
#             temp1.next=temp
            
#         return g
