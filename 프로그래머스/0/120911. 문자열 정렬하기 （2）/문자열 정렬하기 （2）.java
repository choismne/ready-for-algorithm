import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public String solution(String my_string) {
        String[] arr = my_string.split("");
        return Arrays.stream(arr).map(String::toLowerCase).sorted().collect(Collectors.joining(""));
    }
}