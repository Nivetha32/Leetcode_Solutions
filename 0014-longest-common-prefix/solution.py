class Solution:
    def longestCommonPrefix(self, strs):
        if not strs or "" in strs:
            return ""


        prefix = strs[0]

       
        for word in strs[1:]:
            
            while word and not word.startswith(prefix):
                prefix = prefix[:-1]  
                
             
                if not prefix:
                    return ""

        return prefix


