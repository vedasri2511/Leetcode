class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        int i = 0;
        int j = 0;
        HashSet<Integer> set = new HashSet<>();
        while( j < nums.length ){
            if(set.contains(nums[j])){
                return true;
            }
            set.add(nums[j]);
            if(j-i < k){
                j++;
            } else if( j - i == k ){
                set.remove(nums[i]);
                i++;
                j++;
            }
        }
        return false;
    }
}