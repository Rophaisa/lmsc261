const drawing = p5 => {

    p5.setup = () => {
        p5.createCanvas(600, 600);
    }

    p5.draw = () => {
        p5.background(230, 230, 230)

        // circle
        let centerCoords = [p5.width * 0.5, p5.height * 0.5];
        let circleSize = p5.width * 0.7;


        p5.fill(255, 0, 0);
        p5.circle(centerCoords[0], 
                centerCoords[1], 
                circleSize);

        p5.noFill();
        p5.stroke(0);
        p5.strokeWeight(5);
        // dimples
        let dimpLeftCoords = [p5.width * 0.45, p5.height * 0.2]
        let dimpRightCoords = [p5.width * 0.55, p5.height * 0.2]

        p5.line(dimpLeftCoords[0], 
            dimpLeftCoords[1], 
            dimpRightCoords[0],
            dimpRightCoords[1]); 

        // stem 
        let stemCoords = [p5.width * 0.6, p5.height * 0.2];
        let startAngle = Math.PI;
        let endAngle = startAngle + Math.PI * 0.5
        let stemCircleSize = p5.width * 0.2;
        p5.arc(stemCoords[0], 
            stemCoords[1],
            stemCircleSize, 
            stemCircleSize,
            startAngle, 
            endAngle);


    }
}

new p5(drawing);