function checkLifeSpan(hoursUsed) {

const maxLifeSpan = 1000;

    if (typeof hoursUsed !== "number") {
        return "please enter valid number";
    }

    //small800
    if (hoursUsed < 800) {
        return "suit in working condition";
    }

    //800 --- 999 之间
    else if (hoursUsed >= 800 && hoursUsed < maxLifeSpan) {
        return "suit needs replacement soon";
    }

    //>= 1000
    else if (hoursUsed >= maxLifeSpan) {
        return "suit no longer safe to use";
    }
}

let hoursUsed = Number(prompt("How many hours it used?"))

print(checkLifeSpan(hoursUsed));