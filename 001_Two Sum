class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		dic = {}
		for i, num in enumerate(nums):
			if target - num in dic:
				return [dic[target - num], i]
			dic[num] = i
		return []

if __name__ == "__main__":
	Solution = Solution()
	test = [2, 7, 11, 15]
	print(Solution.twoSum(test, 9))  # Example test case
