const conesSoldPerHour = 3;
const inventory = 60; //extra part


for (let hour = 1; hour <= 12; hour++) {
  
    let sold = conesSoldPerHour * hour;

    print (sold + " sold at hour " + hour);

    //剩余库存
    let remaining = inventory - sold;
    
    print (remaining + " left");

}