class Solution {
    public int solution(int order) {
        int answer=0;
        String[] arr = String.valueOf(order).split("");
        for(String value : arr){
            if(value.equals("3")) answer ++;
            else if(value.equals("6")) answer ++;
            else if(value.equals("9")) answer++;
        }
        return answer;
    }
}