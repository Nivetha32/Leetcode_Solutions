class Solution {
    public boolean scoreBalance(String s) {
        int tot =0;
        for(char c : s.toCharArray())
            {
                tot+=c-'a'+1;
            }
        int lefs = 0;
        for(int i=0;i<s.length()-1;i++)
            {
                lefs+=s.charAt(i)-'a'+1;
                int  rights=tot-lefs;
               if(lefs == rights)
                {
            return true;
                }
         }
        return false;
    }
}
