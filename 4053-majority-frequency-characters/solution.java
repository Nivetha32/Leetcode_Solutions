class Solution {
    public String majorityFrequencyGroup(String s) {
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            int in = ch - 'a';
            freq[in]++;
        }

        ArrayList<Character>[] g = new ArrayList[s.length() + 1];
        for (int i = 0; i <= s.length(); i++) {
            g[i] = new ArrayList<>();
        }

        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) {
                g[freq[i]].add((char) ('a' + i));
            }
        }

        int bestK = 0;
        for (int k = 1; k <= s.length(); k++) {
            if (g[k].size() > g[bestK].size() || 
               (g[k].size() == g[bestK].size() && k > bestK)) {
                bestK = k;
            }
        }

        StringBuilder result = new StringBuilder();
        for (char c : g[bestK]) {
            result.append(c);
        }

        return result.toString();
    }
}

