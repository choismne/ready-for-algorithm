class Solution {
    public String solution(String rsp) {
        String answer = "";
        String[] my_string = rsp.split("");
        for(String value : my_string){
            if(value.equals("2")) answer+="0";
            else if(value.equals("0")) answer+="5";
            else if(value.equals("5")) answer+="2";
        }
        return answer;
    }
}