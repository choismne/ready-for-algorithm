import java.util.Arrays;

class Solution {
    public int solution(int[] sides) {
        Arrays.sort(sides);
        if(sides[2] >= sides[0]+sides[1]){
            return 2;
        }
        else
            return 1;
    }
}