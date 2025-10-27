class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        int freq[] = new int[2001];
        Set<Integer> si = new HashSet<>();
        for(int m : arr)
        {
            freq[m+1000]++;
        }
        for(int c: freq)
        {
        if(c>0)
        {
            if(si.contains(c))
            {
                return false;
            }
            si.add(c);
        }
        }
        return true;
    }
}
