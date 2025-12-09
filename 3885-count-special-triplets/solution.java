class Solution {
    public int specialTriplets(int[] nums) {
        int MOD = 1_000_000_007;
        int ms = 100_005;
        long i=0;

        long[] frL = new long[ms];
        long[] frR = new long[ms];

        for(int l : nums)
        {
            frR[l]++;
        }
        for(int y : nums)
        {
            frR[y]--;

            long k = (y*2 <ms) ? frL[y*2]:0;
            long g = (y*2 <ms) ? frR[y*2]:0;

            i = (i+k*g)%MOD;
            frL[y]++;

        }
        return (int)i;
    }
}
