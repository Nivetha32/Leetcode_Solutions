class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        return len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words))) if len(pattern) == len(words) else False

