class Solution {
    public String solution(int age) {
        String answer = "";
        String[] arr = String.valueOf(age).split("");
        for(String value : arr){
            if(value.equals("0")) answer += "a";
            else if(value.equals("1"))answer += 'b';
            else if(value.equals("2"))answer += 'c';
            else if(value.equals("3"))answer += 'd';
            else if(value.equals("4"))answer += 'e';
            else if(value.equals("5"))answer += 'f';
            else if(value.equals("6"))answer += 'g';
            else if(value.equals("7"))answer += 'h';
            else if(value.equals("8"))answer += 'i';
            else if(value.equals("9"))answer += 'j';
        }
        return answer;
    }
}