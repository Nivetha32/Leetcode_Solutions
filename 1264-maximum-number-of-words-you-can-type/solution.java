class Solution {
    public int canBeTypedWords(String text, String brokenLetters) 
    {
        String words[] = text.split(" ");
        
        int co=0;
        for(String word : words)
        {
            boolean c = true;
            for(int j=0;j<brokenLetters.length();j++)
            {
                char ch1 = brokenLetters.charAt(j);
                if(word.indexOf(ch1)!= -1)
                {
                    c=false;
                    break;
                }
            }
            if(c) co++;
        }
        return co;
    }
}
