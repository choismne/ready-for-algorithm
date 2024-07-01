import java.util.Collections;
import java.util.ArrayList;

class Solution {
    public int solution(int[] array) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int value : array){
            list.add(value);
        }
        Collections.sort(list);
        return list.get(list.size()/2);
    }
}