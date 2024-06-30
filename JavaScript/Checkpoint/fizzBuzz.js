fizzBuzz = (num) => {
    for (let i=1; i <= num; i++){
        if (i % 15 === 0){ console.log("FizzBuzz"); continue } // LCM
        if (i % 3 === 0){ console.log("Fizz"); continue }
        if (i % 5 === 0){ console.log("Buzz"); continue }
        console.log(i);
    }
}

fizzBuzz(20)