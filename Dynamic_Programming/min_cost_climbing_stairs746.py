class Solution:
	def minCostClimbingStairsVer1(self, cost: list[int]) -> int:
		#54ms/62.99%  16.63mb/66.99%
		# Bottom Up Dp
		n = len(cost)
		dp = [0] * (n+1)

		for i in range(2, n+1):
			dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])

		return dp[n]

	def minCostClimbingStairsVer2(self, cost: list[int]) -> int:
		#54ms/62.99%  16.59mb/93.69%
		# Bottom Up Dp
		prev = cost[-1]
		cur = cost[-2]
		for i in range(len(cost) -3, -1, -1):
			temp = cost[i] + min(cur, prev)
			prev = cur
			cur = temp
		return min(cur, prev)


print(Solution().minCostClimbingStairs([1,2,3]))



