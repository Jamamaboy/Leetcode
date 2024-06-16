# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


def findMedianSortedArrays(nums1, nums2):
	num = [*nums1, *nums2]
	num.sort()
	l = len(num)
	if  l % 2 == 1:
		return num[l // 2]
	else:
		return (num[l // 2 - 1] + num[l // 2]) / 2

num1 = [1, 2]
num2 = [4]
print(findMedianSortedArrays(num1, num2))
