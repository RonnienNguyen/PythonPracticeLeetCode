import re

class Solution(object):
    def split_string(self, s):
        # Remove all non-letter characters using regex
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        s = s.lower()
        combined_s = s[::-1]
        return combined_s == s

if __name__ == "__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    print(solution.split_string(s))  # Output: True
