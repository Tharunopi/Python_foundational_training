function add(...input){
    sum = 0
    for (let i of input){
        sum += i
        console.log(sum)
    }
    console.log("Grand Sum: " + (sum))
}

add(1, 2, 3, 4, 5, 86487468)