class Solution {
    public String reverseVowels(String s) {
        StringBuilder k = new StringBuilder();
        StringBuilder y = new StringBuilder();
        for(char ch: s.toCharArray())
        {
            if("aeiouAEIOU".indexOf(ch)!=-1)
            {
                k.append(ch);
            }
        }
        k = k.reverse();
        int j=0;
        for(int i=0;i<s.length();i++)
        {
            char ch = s.charAt(i);
            if(ch == 'a' || ch=='e'|| ch=='i'|| ch =='o'|| ch=='u'
            ||ch =='A' || ch=='E'|| ch=='I'|| ch =='O'|| ch=='U')
            {
                     y.append(k.charAt(j++));
            }
            else
            {
                 y.append(ch);
            }
        }
      return y.toString();
    }
}
