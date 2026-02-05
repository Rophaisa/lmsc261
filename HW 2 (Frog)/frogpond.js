let numFrogs = prompt("How many forgs are about to jump in?");
const maxFrogCapacity = 15
let isPondOverCapacity = Number(numFrogs) > maxFrogCapacity;
let messageToPrint = isPondOverCapacity ? "It's too crowded!" : "Come on in!";
print (messageToPrint);

