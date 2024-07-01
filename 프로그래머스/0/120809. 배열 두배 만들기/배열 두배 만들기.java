import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int[] numbers) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int value : numbers){
            list.add(value*2);
        }
        return list;
    }
}