"use strict"

const numFunction = (num1, num2) =>{
    return console.log(num1, num2);
    
}

const welcome = (name, age, gender) =>{
    return console.log(`My name is ${name}, I am ${age} years old and of gender ${gender}`);
    
}

const powerUp = (n1, n2) => {
    return console.log(Math.pow(n1, n2));
    
}

numFunction(2, 3)

welcome("Wojciech", 25, "male")

powerUp(2, 3)