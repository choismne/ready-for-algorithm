function solution(str1, str2) {
    let answer = str1.includes(str2)
    if(answer){
        return 1
    }
    else{
        return 2
    }
}