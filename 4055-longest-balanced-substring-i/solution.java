class Solution {
    public int longestBalanced(String s) {
    String pi= s;
    int n = s.length(), ans = 0;

    for (int i = 0; i < n; i++) {
        int[] freq = new int[26];
        for (int j = i; j < n; j++) {
            freq[s.charAt(j) - 'a']++;

            int val = 0; 
            boolean ok = true;
            for (int f : freq)
                if (f > 0)
                    if (val == 0) val = f;
                    else if (f != val) { 
                        ok = false; break; 
                    }

            if (ok) ans = Math.max(ans, j - i + 1);
        }
    }
    return ans;
    }
}
