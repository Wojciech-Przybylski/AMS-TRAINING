"use strict";

let darthvader = { Allegiance: "Empire", Weapon: "Lightsaber", Sith: "True", Jedi: "False"};

console.log(
`Darth Vader's allegiance is to the ${darthvader.Allegiance}

Darth Vader's weapon of choice is a ${darthvader.Weapon}

Darth Vader is a sith? ${darthvader.Sith}

Darth Vader is a Jedi? ${darthvader.Jedi}`
);

let myArray = ["hello", "everyone"];

console.log(myArray.length);


for (let i = 0; i < myArray.length; i++){
    console.log(myArray[i]);
}

myArray.push("how","are","we");

console.log(myArray.length);

for (let index in myArray){
    console.log(myArray[index]);
}

myArray.shift();

console.log(myArray.length);

for (let index of myArray ){
    console.log(index);
    
};
