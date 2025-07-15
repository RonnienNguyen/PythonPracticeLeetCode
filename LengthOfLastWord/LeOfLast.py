class Solution(object):
    def LengthOfLastWord(self, s):
        spaces = [i for i, c in enumerate(s) if c == ' ']
        reversed_spaces = spaces[::-1]
        print(reversed_spaces)
    
if __name__ == "__main__":
    solution = Solution()
    s = "Hello Meow Meow Moew"
    solution.LengthOfLastWord(s)