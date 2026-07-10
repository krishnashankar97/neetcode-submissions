class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        ans = ""

        for i, c in enumerate(shortest):
            for word in strs:
                if word[i] != c:
                    return ans
            ans += c

        return ans