const drawing = p5 => {

    //1
    p5.setup = () => {
        //2
        p5.createCanvas(600, 600);
    }

    p5.draw = () => {

        
        p5.background(140, 200, 120);
        p5.fill(200, 120, 200) // #1
        p5.circle(300, 300, 30); // #2
        
        for (let circle = 0; circle < 25; circle++) {

            
            let posOffsetX = 50;
            let posScaleX = (500 / 25) * circle;
            let radius = 10;


            if (circle % 4 == 0) {

                radius = 20;

                p5.fill(200, 100, 100);

            } else {
                p5.fill(266, 266, 266);

            }

            
            p5.noStroke();

            p5.circle(posOffsetX + posScaleX, 300, radius);
        }
    }
}

new p5(drawing);