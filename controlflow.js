/*
let numInstruments = prompt("How many instruments do you play?");
let isMultiInstrumentalist = numInstruments > 1;

if (isMultiInstrumentalist){
    print("Wow, you're good!");
} else {
    print("Try your best!");
}
*/



/*
let numInstruments = prompt("How many instruments do you play?");
let isAMusician = numInstruments ==1; //ture if numInstruments is 1

let isMultiInstrumentalist = numInstruments > 1;

if (isAMusician){
    print("Wow, you good.");

} else if (isMultiInstrumentalist) {
    print("Wow, cool!");

} else {
    print("I got it.");
}

*/


/*
let randomTemp = Math.random(); //random between 0 ~ 1
randomTemp = (randomTemp * 20) - 10;
randomTemp = Math.floor(randomTemp);

let isPositive = randomTemp > 0;
let isNegative = randomTemp < 0;
let isZero = randomTemp === 0;

print(randomTemp);

if (isPositive) {
    print("I's getting warmer!");

} else if (isNegative){
    print("Getting cold!");

} else {
    print("Nobody touched the temp")
}

*/
// -10 to 10 range

/*
let midiNote = prompt("Enter midi note");



let isValidMidiNote = midiNote >= 0 && midiNote <= 127;

if (isValidMidiNote){
    print("yay, it's ok");

} else {
    print("quit music");
}
*/
/*
let numBlocks = prompt("How many blocks?");


let blocks = [];
for (let row = 0; row < numBlocks; row++)
{
    for(let col = 0; col < numBlocks; col++)
    {
        if (row < col)

        blocks.push("#");

    }
    print(blocks);
}
*/

let minNameLenth = true
let nameInput;

while (minNameLenth)
{
    nameInput = prompt("Please enter name");
    if (nameInput.length >=6)
    {
        minNameLenth = false
    }
}

