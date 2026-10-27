class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join([a.lower() for a in s if a.isalnum()])

        return clean[::-1] == clean