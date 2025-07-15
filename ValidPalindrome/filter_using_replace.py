class Solution(object):
    def split_string(self, s):
        s = s.replace(",", "")
        s = s.replace(":", "")
        s = s.lower()
        s = s.strip().split()
        combined = ''.join(s)
        combined_s = combined[::-1]
        if (combined_s == combined):
            return True
        return False
if __name__ == "__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    print(solution.split_string(s))