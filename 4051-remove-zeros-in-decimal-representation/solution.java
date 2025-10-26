class Solution {
    public long removeZeros(long n) {
        String de = String.valueOf(n);
        StringBuilder m = new StringBuilder();
        for(int i =0;i<de.length();i++)
            {
              char ch = de.charAt(i);
                if(ch!='0')
                {
                    m.append(ch);
                }
            }
        return Long.parseLong(m.toString());
        
    }
}
