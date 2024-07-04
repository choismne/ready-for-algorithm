import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(String my_string) {
        ArrayList<Character> answer = new ArrayList<>();
        for(int i=0 ; i<my_string.length() ; i++){
            if(my_string.charAt(i) >= '0' && my_string.charAt(i) <= '9'){
                answer.add(my_string.charAt(i));
            }
        }
        Collections.sort(answer);
        return answer.stream().mapToInt(c -> Character.getNumericValue(c)).toArray();
        
    }
}