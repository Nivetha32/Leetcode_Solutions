class Solution {
    public boolean isPalindrome(String s) {
        String c = s.replaceAll("[^a-zA-Z0-9]","").toLowerCase();
        return c.equals(new StringBuilder(c).reverse().toString());
    }
}
