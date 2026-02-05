
/*
// making semester exist in the world
let semester = 5;
print(semester);

semester = 6; // we can change semester
print(semester);

// immutable variable can't change
const major = "permormance";
print(major);

major = "compostition"; // trying to reassign an immutable variable
print(major);

以上都是被注释掉的
*/

/*
let firstName = "Rophasia";
print(firstName);

let nameUC = firstName.toUpperCase();
print(nameUC);

let nameLC = firstName.toLowerCase();
print(nameLC);

let nameLength = firstName.length;
print(nameLength);

现在开始学numbers */

/*
let num1 = 10; // integer or int
let num2 = 20.5; //float

print(num1 - num2); // 
print(num1 * num2); //各种算法等等 + - * / 。。。。 */

//Boolean
/*
let myBodyAlcohoAmount = prompt("How much did you drink?")
const drinkingLimit = 8;
let didyouSeeMeDrunk = myBodyAlcohoAmount >= drinkingLimit;
*/

// ternary operators

/*
print("Did you see me drunk?")
print(didyouSeeMeDrunk);

let messageToPrint = didyouSeeMeDrunk ? "Go home dombass" : "keep on parting!";
print(messageToPrint)
*/

//Arrays: Storing ultiple Values

/*
let fruits = ["Kiwi", "Pear", "Banana", "Lime" ] //后面的东西是从0开始数的，0.1。2.3...
print(fruits);
let fruit1 = fruits[1];
print(fruit1);
*/

/*
let meals = [];

meals.push("Currry")
print(meals);

meals.push("Burritos");
print(meals);
*/

let workouts = [];

workouts.push(prompt("What's your first workout?"));
workouts.push(prompt("What's your second workout?"));
workouts.push(prompt("What's your third workout?"));
workouts.push(prompt("What's your fourth workout?"));


print(workouts);

let randomNumber = Math.random() * 4;
randomNumber = Math.floor(randomNumber)

print("Your workout today is: ");
print(workouts[randomNumber]);
