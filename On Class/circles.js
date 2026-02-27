const drawing = p5 => {

    p5.setup = () => {
        p5.createCanvas(600, 600);
    }

    p5.draw = () => {
        p5.background(230, 230, 230) //颜色RGB

        for(let cir = 0; cir < 12; cir++)
        {
            let offset = p5.width  * 0.1
            let scale = p5.mouseY * cir

            let radius = 40;
            let newRadius = cir % 3 == 0 //boolean

            p5.circle(offset + scale, 300, 40); //X轴，Y轴，大小
            p5.noStroke();
            p5.fill(216, 170, 185);
        }
    }
}

new p5(drawing); 