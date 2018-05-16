class Solution:
    def isValid(self, s):
        if s == '':
            return True
        sList = list(s)
        stack = []
        for chr in sList:
            if len(stack) == 0:
                stack.append(chr)
            else:
                stack.pop() if (chr == ')' and stack[-1] == '(') or (chr == ']' and stack[-1] == '[') or (
                        chr == '}' or stack[-1] == '{') else stack.append(chr)
        return True if len(stack) == 0 else False

if __name__ == '__main__':
    s = "{{)}"
    hh = Solution().isValid(s)
    print(hh)