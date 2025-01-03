class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
		carry = 0
		current = dummy = ListNode()
		while l1 or l2 or carry:
			val1 = l1.val if l1 else 0
			val2 = l2.val if l2 else 0

			total = val1 + val2 + carry
			carry = total // 10
			node_val = total % 10
			dummy.next = ListNode(node_val)

			if l1:
				l1 = l1.next
			if l2:
				l2 = l2.next
			dummy = dummy.next

		return current.next
		# for i in range(len(l1)):
		# 	l1[i] = str(l1[i])
		# 	l2[i] = str(l2[i])
		# l1 = int("".join(l1[::-1]))
		# l2 = int("".join(l2[::-1]))
		# ans = l1+l2
		# ans = list(str(ans))
		# ans = [int(i) for i in ans]
		# return ans[::-1]

		# max_len = max(len(l1), len(l2))
		# for i in range(max_len-len(l1)):
		# 	l1.append(0)
		# for i in range(max_len-len(l2)):
		# 	l2.append(0)
		# ans = []
		# carry = 0
		# for i in range(max_len):
		# 	ans.append((l1[i]+l2[i]+carry)%10)
		# 	carry = (l1[i]+l2[i]+carry)//10
		# if carry:
		# 	ans.append(carry)
		# return ans

def list_to_listnode(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to convert a ListNode to a list
def listnode_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    solution = Solution()
    test_list1 = [2, 4, 3]  # Represents the number 342
    test_list2 = [5, 6, 4]  # Represents the number 465

    # Convert lists to ListNode
    l1 = list_to_listnode(test_list1)
    l2 = list_to_listnode(test_list2)

    # Call the function and convert the result back to a list
    result_node = solution.addTwoNumbers(l1, l2)
    result_list = listnode_to_list(result_node)

    print(result_list)  # Output: [7, 0, 8] (Represents the number 807)
