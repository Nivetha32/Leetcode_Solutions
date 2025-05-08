class Solution {
    int reverse(int x) {
        int max_int = 2147483647, min_int = -2147483648;
        int r_x = 0;
        while (x != 0) {
            int k = x % 10;
            x /= 10;
            if (r_x > max_int / 10 || (r_x == max_int / 10 && k > 7)) return 0;
            if (r_x < min_int / 10 || (r_x == min_int / 10 && k < -8)) return 0;
            r_x = r_x * 10 + k;
        }
        return r_x;
    }
}
