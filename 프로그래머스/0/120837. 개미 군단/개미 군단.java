class Solution {
    public int solution(int hp) {
        int answer = 0;
        int namoji = 0;
        answer += hp/5;
        namoji = hp%5;
        answer += namoji/3;
        namoji = namoji%3;
        answer += namoji;
        return answer;
    }
}