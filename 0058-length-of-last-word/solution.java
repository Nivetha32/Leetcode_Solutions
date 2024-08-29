class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        int length = s.length();
        int index = length - 1;
        
        while (index >= 0 && s.charAt(index) != ' ') {
            index--;
        }
        
        return length - index - 1;
    }
    
    
}
