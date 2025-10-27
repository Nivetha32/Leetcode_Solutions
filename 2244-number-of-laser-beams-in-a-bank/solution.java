class Solution {
    public int numberOfBeams(String[] bank) {
        int prev =0, an =0;
        for(String ro : bank)
        {
            int cu =0;
            for(char c : ro.toCharArray())
              if(c == '1') cu++;
            if(cu >0)
            {
                an+=prev *cu;
                prev = cu;
            }
        }
        return an;
    }
}
