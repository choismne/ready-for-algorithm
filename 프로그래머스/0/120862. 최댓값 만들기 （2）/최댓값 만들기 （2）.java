import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        int len = numbers.length;
        int[] sortedNumbers = Arrays.stream(numbers).sorted().toArray();
        if(sortedNumbers[0]*sortedNumbers[1] > sortedNumbers[len-1]*sortedNumbers[len-2]){
            return sortedNumbers[0]*sortedNumbers[1];
        }
        else{
            return sortedNumbers[len-1]*sortedNumbers[len-2];
        }
    }
}