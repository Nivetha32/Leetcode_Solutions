class Solution {
    public boolean halvesAreAlike(String s) {
        int n = s.length();
        int c=0;
        int k=0;
        String vow = "aeiouAEIOU";
        for(int i=0;i<s.length();i++)
        {
            char ch =s.charAt(i);
            if(vow.indexOf(ch)!=-1)
            if(i<n/2)
              {
            c++;
             }
            else
              {
            k++;
              }
        }
        return c==k;
        
    }
}
