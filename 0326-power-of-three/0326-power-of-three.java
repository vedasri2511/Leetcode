class Solution {
    public boolean isPowerOfThree(int n) {
        if (n <= 0) return false;
        
        long power = 1;
        
        while (power < n) {
            power = power * 3;
        }
        
        return power == n;
    }
}