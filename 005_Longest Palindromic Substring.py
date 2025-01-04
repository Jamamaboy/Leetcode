class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        Max_Len=1
        Max_Str=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > Max_Len:
                        Max_Len = i-j+1
                        Max_Str = s[j:i+1]
        return Max_Str

#Test cases
test_cases = [
	("babad", "bab"),
	("cbbd", "bb")
]

#Output
solution = Solution()
for i, (s, expected) in enumerate(test_cases):
	result = solution.longestPalindrome(s)
	assert result == expected, f"Test case {i + 1} failed: input = {s}, expected = {expected}, got = {result}"
	print(f"Test case {i + 1} passed")
print("All tests passed. XD")


