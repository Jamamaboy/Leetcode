import math
class Solution:
	def uniquePathsD2(self, m: int, n: int) -> int:
		# 2 D map
		# m == row
		# n == col

		dp = [[1 if row == 0 or col == 0 else 0 for col in range(n)] for row in range(m)]
		# dp = [[0 for col in range(n)] for row in range(m)]
		# for col in range(m): dp[0][col] = 1
		# for row in range(n): dp[row][0] = 1
		# #	x 	 n n n
		# #	m [	[1 1 1],
		# #	m	[1 0 0],
		# #	m	[1 0 0]]
		for row in range(1, m):
			for col in range(1, n):
				dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

		return dp[-1][-1]

	def uniquePathsD2Patch2(self, m: int, n: int) -> int:
		# 2 D map
		# m == row
		# n == col
		dp = [[1] * n] * m
		for row in range(1, m):
			for col in range(1, n):
				dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

		return dp[-1][-1]


	def uniquePathsD1(self, m: int, n: int) -> int:
		...


	def uniquePathsMath(self, m: int, n: int) -> int:
		#  (m+n-2)!
		# -----------
		# (m-1)!(n-1)!
		return math.comb(m+n-2, m-1)



print(Solution().uniquePaths(4,2))
