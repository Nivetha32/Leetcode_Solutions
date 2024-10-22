class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        int minIndexSum = Integer.MAX_VALUE;
        int count = 0;
        for (int i = 0; i < list1.length; i++) {
            for (int j = 0; j < list2.length; j++) {
                if (list1[i].equals(list2[j])) {
                    int indexSum = i + j;
                    if (indexSum < minIndexSum) {
                        minIndexSum = indexSum;
                        count = 1;  
                    } else if (indexSum == minIndexSum) {
                        count++;  
                    }
                }
            }
        }

        String[] result = new String[count];
        int k = 0;
        for (int i = 0; i < list1.length; i++) {
            for (int j = 0; j < list2.length; j++) {
                if (list1[i].equals(list2[j]) && (i + j == minIndexSum)) {
                    result[k++] = list1[i];  
                }
            }
        }

        return result;
    }
}

