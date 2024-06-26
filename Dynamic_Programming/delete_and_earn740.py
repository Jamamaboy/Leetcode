class Solution:
	def deleteAndEarn(self, nums: list[int]) -> int:

		num_lookup = [0] * (max(nums) + 1)
		for n in nums:
			num_lookup[n] += n
		# num_lookup = [0{0}, 1,{0}, 2{2*2}, 3{3*3}, 4{4*1})]
		# num_loolup = [0, 0, 4, 9, 4]
		dp = [0] * len(num_lookup)
		# len(num_lookup) = 5
		dp[1] = num_lookup[1]
		# dp = [0,0,0,0,0]
		for n in range(2, len(num_lookup)):
			dp[n] = max(num_lookup[n] + dp[n - 2], dp[n -1])
		# dp = [0, 0, 4, 0, 0]
		# dp = [0, 0, 4, 9, 0]
		# dp = [0, 0, 4, 9, 9]
		return dp[-1]

nums = [2,2,3,3,3,4]
print(Solution().deleteAndEarn(nums))

