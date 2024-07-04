class Solution {
    public String solution(String my_string, int num1, int num2) {
        String answer = "";
        String[] arr = my_string.split("");
        String tmp = arr[num1];
        arr[num1] = arr[num2];
        arr[num2] = tmp;
        for(String value : arr){
            answer += value;
        }
        return answer;
    }
}