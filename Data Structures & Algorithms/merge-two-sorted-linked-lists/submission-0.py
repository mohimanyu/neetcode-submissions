# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        result_list = ListNode(0)
        head = result_list

        list1_curr = list1
        list2_curr = list2

        while list1_curr and list2_curr:
            if list1_curr.val <= list2_curr.val:
                result_list.next = list1_curr
                list1_curr = list1_curr.next
            else:
                result_list.next = list2_curr
                list2_curr = list2_curr.next
            result_list = result_list.next
        
        if list1_curr:
            result_list.next = list1_curr
        
        if list2_curr:
            result_list.next = list2_curr

        return head.next
