class Solution {
    public boolean isValid(String word) {
        if(word.length()<3)   return false;
        boolean b = false;
        boolean v = false;
        boolean comn = false;
        for(char ch : word.toCharArray())
        {
            if(!Character.isLetterOrDigit(ch)) return false;
            if(Character.isLetter(ch))
            {
                char c = Character.toLowerCase(ch);
                if("aeiou".indexOf(c)!=-1)
                {
                    v=true;
                }
                else
                {
                    comn=true;
                }
            }
        }
        return v && comn;
    
    }
}
        
