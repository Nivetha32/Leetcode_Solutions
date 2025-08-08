class Solution {
    public int countOdds(int l, int h) {
        return (h - l) / 2 + ((l % 2 != 0 || h % 2 != 0) ? 1 : 0);
    }
}

