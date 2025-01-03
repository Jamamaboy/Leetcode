class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        point = 0
        max_length = 0
        for i, char in enumerate(s):
            if char in seen:
                point = max(point, seen[char] + 1)
            seen[char] = i
            max_length = max(max_length, i - point + 1)
        return max_length

# Test cases
test_cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    (" ", 1),
    ("au", 2)]

# Output:
solution = Solution()
print("Running tests...")
for i, (s, expected) in enumerate(test_cases):
    result = solution.lengthOfLongestSubstring(s)
    assert result == expected, f"Test case {i + 1} failed: input={s}, expected={expected}, got={result}"
    print(f"Test case {i + 1} passed")
print("All tests passed. :)")
