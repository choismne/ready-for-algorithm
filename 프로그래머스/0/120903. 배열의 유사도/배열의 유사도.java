class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        for(String value1 : s1){
            for(String value2 : s2){
                if(value1.equals(value2)) answer++;
            }
        }
        return answer;
    }
}