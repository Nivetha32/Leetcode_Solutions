class Solution {
    public int numberOfBeams(String[] bank) {
       int prev = 0;
       int total = 0;
       for(String r : bank)
       {
       int cur=0;
           for(char ch : r.toCharArray())
              {
                  if(ch =='1') cur++;
              }
           if(cur>0)
            {
                total+=prev*cur;
                prev=cur;
             }
       }
       return total;
    }
}
