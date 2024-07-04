import java.util.ArrayList;
class Solution {
    public ArrayList solution(int[] numbers, String direction) {
        ArrayList<Integer> arr = new ArrayList<>();
        int tmp;
        for(int value : numbers){
            arr.add(value);
        }
        if(direction.equals("right")){
            tmp = arr.remove(numbers.length-1);
            arr.add(0, tmp);
        }
        else{
            tmp = arr.remove(0);
            arr.add(tmp);
        }
        return arr;
    }
}