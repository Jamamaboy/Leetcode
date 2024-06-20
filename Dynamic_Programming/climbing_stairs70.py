
class Solution:
		def climbStairs(self, n: int) -> int:
			if (n == 1 or n == 2):
				return n
			a = [1, 1]

			for _ in range(n - 1):
				a.append(a[-1] + a[-2])

			return a[-1]

print(Solution().climbStairs(1))

		# fibonacci = [0,1]

		# for i in range (2, n + 2):
		# 	fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

		# return fibonacci[-1]
