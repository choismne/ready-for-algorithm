class Solution {
    public int solution(int n) {
        int s = (int)Math.sqrt(n);
        if(s*s == n)return 1;
        else return 2;
    }
}