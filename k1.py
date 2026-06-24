class Solution {
    public int reverseExponentiation(int n) {
        // code here
        if(n==10){return n;}
        int k=n;
        for (int i=2;i<=n;i++){
            k=k*n;
        }
        return k;
    }
}
