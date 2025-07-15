class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.strip().split()
        if not words:
            return 0
        print(words)
        return len(words[-1])

if __name__ == "__main__":
    solution = Solution()
    s = "   fly me   to   the moon  "
    print(solution.lengthOfLastWord(s))  # Output: 4
