class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x < 0:
			return False
		return str(x) == str(x)[::-1]

#Test cases
test_cases = [
	(-42, False),
	(424, True)
]

#Output
solution = Solution()
for i, (s, expected) in enumerate(test_cases):
	result = solution.isPalindrome(s)
	assert result == expected, f"Test case {i + 1} failed: input = {s}, expected = {expected}, got = {result}"
	print(f"Test case {i + 1} passed")
print("All tests passed. XD")


