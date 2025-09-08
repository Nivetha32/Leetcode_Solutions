class Solution {
    public String reverseWords(String s) {
        String k[] = s.trim().split("\\s+");
        StringBuilder sb  = new StringBuilder();
        for(int i=k.length-1;i>=0;i--)
        {
            sb.append(k[i]).append(" ");
        }
        return sb.toString().trim();
    }
}
