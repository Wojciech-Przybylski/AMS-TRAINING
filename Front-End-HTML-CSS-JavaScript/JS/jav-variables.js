// "use strict";

// let a;
// let b = "12345";
// let c = 12344;
// let d = true;
// let e = {a:"JavaScript"};

// console.log(typeof(a));
// console.log(typeof(b));
// console.log(typeof(c));
// console.log(typeof(d));
// console.log(typeof(e));


// let totalMoney = 4000;
// let moneyPaidSoFar = 2348;
// let totalLeftToPay = totalMoney - moneyPaidSoFar;

// console.log(`Total bill is £${totalMoney} and the remaining amount to pay is £${totalLeftToPay}`)


// //iterations 


// let loop1 = 100;
// while (loop1 <= 200) {
//     loop1++;
//   console.log(loop1);
// }

// let loop2 = 100;
// while (loop2 <= 200) {
//   if (loop2 % 2 == 0) {
//     console.log("-");
//   } else {
//     console.log("*");
//   }
//   a++;
// }

// for (let i = 0; i < 10; i++) {
//     for (let j = 1; j <= 10; j++) {
//       console.log(j);
//     }
//  }  

//  for (let loop3 = 100; loop3 <= 200; loop3++) {
//     console.log(loop3);
//   }
  
// let strictA = true;
// let strictB = 1;

// alert(strictA == strictB); // True 
// alert(strictA === strictB); // False

// alert(strictA != strictB); // false
// alert(strictA !== strictB); // true
 
let age = 10

// if (age >= 18 && age <= 65) {
//     alert("in age range")
// }
// else if (age < 18){
//     alert("is underage")
// }
// else{
//     alert("is older than 65")
// }

// agecheck = (age >= 50)? "is 50 or over" : "is under 50"
// alert(agecheck)


let lowertoday

while (true) {

    let today = prompt("Enter todays day");
    let lowertoday = today.toLowerCase();

switch (lowertoday) {
    case "monday":
    case "tuesday":
    case "wednesday":
    case "thursday":
    case "friday":
        alert("it's a weekday!")
        break;
    case "saturday":
        alert("it's Saturday!")
        break;
    case"sunday":
        alert("it's Sunday!")
        break;
      default:
        alert("incorrect value! try again");
        continue;
}
break;
}