class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder merged = new StringBuilder();  // Step 1: Use StringBuilder for efficiency
        int i = 0, j = 0;  // Step 2: Initialize two pointers

        // Step 3: Loop to merge alternately
        while (i < word1.length() && j < word2.length()) {
            merged.append(word1.charAt(i++));  // Add from word1 and move pointer
            merged.append(word2.charAt(j++));  // Add from word2 and move pointer
        }

        // Step 4: Append the remaining characters (if any)
        if (i < word1.length()) merged.append(word1.substring(i));
        if (j < word2.length()) merged.append(word2.substring(j));

        return merged.toString();  // Step 5: Convert StringBuilder to String
    }
}

