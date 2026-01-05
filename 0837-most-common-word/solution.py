class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ke = re.findall(r'\w+', paragraph.lower()) 
        k = Counter(i for i in ke if i not in banned)
        return k.most_common(1)[0][0]
