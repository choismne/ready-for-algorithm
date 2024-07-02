import java.util.ArrayList;

class Solution {
    public ArrayList solution(int n, int[] numlist) {
        ArrayList<Integer> answer = new ArrayList<>();
        for(int value : numlist){
            if(value%n == 0){
                answer.add(value);
            }
        }
        return answer;
    }
}