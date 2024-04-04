function solution(num_list) {
    var answer = [], sum_1 = 0, sum_2 = 0
    for(var i of num_list){
        if(i%2 === 0){
            sum_1 += 1
        }
        else
            sum_2 += 1
    }
    answer.push(sum_1)
    answer.push(sum_2)
    return answer;
}