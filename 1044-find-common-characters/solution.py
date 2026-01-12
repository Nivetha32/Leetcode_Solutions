class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        m = Counter(words[0])

        for word in words[1:]:
           m&=Counter(word)
        return list(m.elements())
    


