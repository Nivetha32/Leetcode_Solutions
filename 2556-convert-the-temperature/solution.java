class Solution {
    public double[] convertTemperature(double celsius) {
        double kelvin = celsius +273.15;
        double farenheit = celsius *1.80 + 32.00;
        double arr[]= {kelvin,farenheit};
        return arr;
    }
}
