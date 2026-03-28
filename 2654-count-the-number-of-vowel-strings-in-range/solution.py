class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        c = 0
        for word in words[left:right+1]:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                  c+=1
        return c
