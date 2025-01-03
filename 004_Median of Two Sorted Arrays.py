class Solution:
	def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

		def mergelist(nums1, nums2):
			newlist = []
			p1, p2 = 0, 0
			while p1 < len(nums1) and p2 < len(nums2):
				if nums1[p1] <= nums2[p2]:
					newlist.append(nums1[p1])
					p1+=1
				else:
					newlist.append(nums2[p2])
					p2+=1

			if p1 < len(nums1):
				newlist.extend(nums1[p1:])
			if p2 < len(nums2):
				newlist.extend(nums2[p2:])

			return newlist

		merged = mergelist(nums1, nums2)
		n = len(merged)
		if n % 2 == 1:
			median = merged[n // 2]
		else:
			median = (merged[n // 2 - 1] + merged[n // 2]) / 2
		return median


#Test cases
test_cases = [
	([1,3], [2], 2.00000),
	([1,2], [3,4], 2.50000)
]

#Output
solution = Solution()
for i, (nums1, nums2, expected) in enumerate(test_cases):
	result = solution.findMedianSortedArrays(nums1, nums2)
	assert result == expected, f"Test case {i + 1} failed: input = {nums1}, {nums2}, expected = {expected}, got = {result}"
	print(f"Test case {i + 1} passed")
print("All tests passed. XD")

