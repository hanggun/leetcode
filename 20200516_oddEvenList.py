# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:09:09 2020

@author: Administrator
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #Set two head node of two new Listnode
        for_odd = ListNode(0)
        for_even = ListNode(0)
        
        #Store the head of each new Listnode
        odd_head = for_odd
        even_head = for_even
        
        #Set the first flag to odd
        is_odd = True
        
        #check whether head is to end
        while head:
            
            #put odd index number to odd list and vise versa
            if is_odd:
                for_odd.next = head
                for_odd = for_odd.next
            else:
                for_even.next = head
                for_even = for_even.next
                
            #move to the next node
            is_odd = not is_odd
            head = head.next
            
        #put None value to the last node of even list
        for_even.next = None
        
        #put two list together
        for_odd.next = even_head.next
        
        return odd_head.next
    
    def createListNode(self, nums):
        
        node = ListNode(nums[0])
        node_head = node
        
        for i in nums[1:]:
            node.next = ListNode(i)
            node = node.next
            
        return node_head
    
    def printInorder(self, root): 
        if root is None: 
            return 
        print(root.val)
        self.printInorder(root.next) 

nums = [2,1,3,5,6,4,7,None]
solution = Solution()
head = solution.createListNode(nums)
solution.printInorder(head)
odd_even = solution.oddEvenList(head)
print('-'*15)
solution.printInorder(odd_even)