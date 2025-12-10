class Solution {
    public char findTheDifference(String s, String t) {
        int m=0;
        for(char l : s.toCharArray())
        {
            m^=l;
        }
        for(char l : t.toCharArray())
        {
            m^=l;
        }
      return (char)m;
    }
}
