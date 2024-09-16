class NumArray {
    private int[] ps;

    public NumArray(int[] n) {
        ps = new int[n.length + 1];
        for (int i = 0; i < n.length; i++) {
            ps[i + 1] = ps[i] + n[i];
        }
    }

    public int sumRange(int i, int j) {
        return ps[j + 1] - ps[i];
    }
}

