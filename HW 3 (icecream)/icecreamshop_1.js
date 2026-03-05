const priceOfIceCream = 5;

let paymentRecieved = Number(prompt("This icecream costs $5, how much money do you have?"));
let isPaymentEnough = false;

if (paymentRecieved >= priceOfIceCream) {

    
    isPaymentEnough = true;

    
    let changeNumber = paymentRecieved - priceOfIceCream;
    print ("Thanks! Enjoy the Ice Cream! This are your change" + changeNumber);

} else {

   
    print ("Not enough cash!");

}