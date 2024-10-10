class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        
        int c = 0; 
        int cookie = 0; 
        
        while (c < g.length && cookie < s.length) {
            if (s[cookie] >= g[c]) {
                c++;
            }
            cookie++;
        }
        
        return c; 
    }
}

