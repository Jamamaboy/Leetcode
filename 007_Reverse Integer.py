class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  # ขอบเขตของ signed 32-bit integer

        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_x = int(str(x)[::-1])

        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0

        return sign * reversed_x

#Test cases
test_cases = [
	(123, 321),
    (-123, -321)
]

#Output
solution = Solution()
for i, (s, expected) in enumerate(test_cases):
	result = solution.reverse(s)
	assert result == expected, f"Test case {i + 1} failed: input = {s}, expected = {expected}, got = {result}"
	print(f"Test case {i + 1} passed")
print("All tests passed. XD")


