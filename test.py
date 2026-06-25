// Online Java Compiler
// Use this editor to write, compile and run your Java code online
class Solution {
    public void kd(int[] nums, int val) {
    int count=0;
    int j=0;
    int k=nums.length-1;
    while(j<k){
        while(j<=k && nums[k]==val){
            count++;
            k--;
        }
        if(j>k){break;}
        if(nums[j]==val){
            int temp=nums[j];
            nums[j]=nums[k];
            nums[k]=temp;
            count++;
        }
        j++;

        
    }
    System.out.println(nums);
    System.out.println(count);
    return ;
    }
}
class Main {
    public static void main(String[] args) {
        Solution k=new Solution();
        int [] nums={1,2,2,4,2};
        int val=2;
        k.kd(nums,val);
    }
} 