class Solution {
    public int cal1(int a, int b){
        String tmp = Integer.toString(a) + Integer.toString(b);
        int ret = Integer.parseInt(tmp);
        return ret;
    }
    public int cal2(int a, int b){
        return 2*a*b;
    }
    public int solution(int a, int b) {
        int ans1 = cal1(a, b);
        int ans2 = cal2(a, b);
        if(ans1 > ans2){
            return ans1;
        }
        else{
            return ans2;
        }
    }
}