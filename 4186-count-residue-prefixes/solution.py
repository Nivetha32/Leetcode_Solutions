class Solution:
    def residuePrefixes(self, s: str) -> int:
        pre = set()
        c=0
        for i in range(len(s)):
            pre.add(s[i])
            prefi_len=i+1
            if len(pre) == prefi_len%3:
                c+=1
        return c
