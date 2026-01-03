class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        INF = 10**18
        m_val = [INF]*n

        m_val[0]=0

        for i,v in restrictions:
            m_val[i] = min(m_val[i],v)
        for i in range(1,n):
            m_val[i] = min(m_val[i],m_val[i-1]+diff[i-1])
        for i in range(n-2,-1,-1):
            m_val[i]= min(m_val[i],m_val[i+1]+diff[i])
        return max(m_val)
