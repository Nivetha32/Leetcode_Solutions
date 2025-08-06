class Solution {
    public String addStrings(String num1, String num2) {
        int i = num1.length() - 1;
        int j = num2.length() - 1;
        int c = 0;
        String s = "";

        while (i >= 0 || j >= 0 || c > 0) {
            int x = (i >= 0) ? num1.charAt(i--) - '0' : 0;
            int y = (j >= 0) ? num2.charAt(j--) - '0' : 0;
            int z = x + y + c;
            c = z / 10;
            s = (z % 10) + s;
        }

        return s;
    }
}

