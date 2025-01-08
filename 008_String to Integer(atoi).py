class Solution:
	def myAtoi(self, s: str) -> int:
		# Define INT_MIN and INT_MAX
		INT_MIN, INT_MAX = -2**31, 2**31 - 1
		i, n = 0, len(s)

		# Skip leading spaces
		while i < n and s[i] == ' ':
			i += 1

		# Handle optional sign
		sign = 1
		if i < n and s[i] == '-':
			sign = -1
			i += 1
		elif i < n and s[i] == '+':
			i += 1

		# Convert digits to integer
		result = 0
		while i < n and s[i].isdigit():
			digit = int(s[i])
			result = result * 10 + digit
			i += 1

		if result < INT_MIN:
			return INT_MIN
		if result > INT_MAX:
			return INT_MAX

		return sign * result



test_cases = [
	"42",                   # 42
	"   -42",               # -42
	"4193 with words",      # 4193
	"words and 987",        # 0
	"-91283472332",         # -2147483648 (INT_MIN)
	"91283472332",          # 2147483647 (INT_MAX)
	"",                     # 0
	"   +0 123",            # 0
	"00000-42a1234",        # 0
	"1337c0313",			# 1337
]

solution = Solution()
for s in test_cases:
	print(f'Input: "{s}" -> Output: {solution.myAtoi(s)}')


