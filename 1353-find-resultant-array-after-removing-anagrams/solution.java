class Solution {
    public List<String> removeAnagrams(String[] words) {
        List<String> result = new ArrayList<>();
        if (words.length == 0) return result;

     
        result.add(words[0]);

        for (int i = 1; i < words.length; i++) {
            String prev = result.get(result.size() - 1);
            String curr = words[i];

            if (!areAnagrams(prev, curr)) {
                result.add(curr);
            }
        }

        return result;
    }
    private boolean areAnagrams(String a, String b) {
        if (a.length() != b.length()) return false;

        char[] arr1 = a.toCharArray();
        char[] arr2 = b.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);

        return Arrays.equals(arr1, arr2);
    }
}

