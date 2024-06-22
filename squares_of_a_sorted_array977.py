class Solution:
	def sortedSquares(self, nums: list[int]) -> list[int]:
		n = len(nums)
		res = [0] * n
		L, R = 0, n - 1
		# left, right = 0 , n - 1

		for i in range(n - 1, -1, -1):
			if (abs(nums[L]) > abs(nums[R])):
				val = nums[L]
				L += 1
			else:
				val = nums[R]
				R -= 1

			res[i] = val ** 2

		return res

print(Solution().sortedSquares([1,2,100,0]))
