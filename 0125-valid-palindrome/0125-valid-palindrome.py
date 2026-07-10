class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()                  # Convert to lowercase
        cleaned = ""

        for ch in s:
            if ch.isalnum():           # Keep only letters and numbers
                cleaned += ch

        return cleaned == cleaned[::-1]