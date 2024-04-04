function solution(my_string) {
    vowels = ['a', 'e', 'i', 'o', 'u']
    return my_string.split('').filter(char => !vowels.includes(char)).join('');
}