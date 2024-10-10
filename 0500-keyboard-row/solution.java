
  class Solution {
    public String[] findWords(String[] w) {
        String r1 = "qwertyuiop";
        String r2 = "asdfghjkl";
        String r3 = "zxcvbnm";
        
        List<String> res = new ArrayList<>();
        
        for (String word : w) {
            String lw = word.toLowerCase();
            if (canType(lw, r1) || canType(lw, r2) || canType(lw, r3)) {
                res.add(word);
            }
        }
        
        return res.toArray(new String[0]);
    }
    
    private boolean canType(String lw, String r) {
        for (char c : lw.toCharArray()) {
            if (r.indexOf(c) == -1) {
                return false;
            }
        }
        return true;
    }
}

