class Solution {
    public int solution(int order) {
        int answer=0;
        String[] arr = String.valueOf(order).split("");
        for(String value : arr){
            if(value.equals("3") || value.equals("6") || value.equals("9")) answer++;
        }
        return answer;
    }
}