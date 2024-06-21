# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         def linked_list_to_int(node):
#             num = 0
#             place = 1
#             while node:
#                 num += node.val * place
#                 place *= 10
#                 node = node.next
#             return num

#         def int_to_linked_list(num):
#             if num == 0:
#                 return ListNode(0)
#             dummy_head = ListNode(0)
#             current = dummy_head
#             while num > 0:
#                 current.next = ListNode(num % 10)
#                 current = current.next
#                 num //= 10
#             return dummy_head.next

#         int_l1 = linked_list_to_int(l1)
#         int_l2 = linked_list_to_int(l2)
#         total = int_l1 + int_l2

#         return int_to_linked_list(total)
