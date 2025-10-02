class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
         int full = numBottles;
        int empty = 0;
        int totalDrunk = 0;
        int exchangeCost = numExchange;

        while (full > 0) {
            totalDrunk += full;
            empty += full;
            full = 0;

            if (empty >= exchangeCost) {
                full = 1;
                empty -= exchangeCost;
                exchangeCost++;
            }
        }
        return totalDrunk;
    }
}
