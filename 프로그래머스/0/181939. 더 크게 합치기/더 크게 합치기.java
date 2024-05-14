class Solution {
    public int plusminus(int a, int b){
        String tmp = Integer.toString(a) + Integer.toString(b);
        int ret = Integer.parseInt(tmp);
        return ret;
    }
    public int solution(int a, int b) {
        int tmp1 = plusminus(a, b);
        int tmp2 = plusminus(b, a);
        
        if(tmp1 > tmp2){
            return tmp1;
        }
        else{
            return tmp2;
        }
    }
}