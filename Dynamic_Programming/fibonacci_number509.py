class Solution:
	def fib(self, n: int) -> int:
		if n <= 1:
			return 1
		return self.fib(n) + self.fib(n-1)

	def fib(self, n: int) -> int:
		if n <= 1:
			return n
		f = [0] * (n + 1)

		f[0] = 1
		f[1] = 1
		for i in range(2, n + 1):
			f[i] = f[i - 1] + f[i - 2]

		return f[-1]

print(Solution().fib2(2))
