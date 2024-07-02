class Solution {
    public int solution(int slice, int n) {
        int answer = (int)Math.ceil((float)n/slice);
        return answer;
    }
}