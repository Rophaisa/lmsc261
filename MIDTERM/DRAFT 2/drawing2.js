function drawCat(p5, x, y, width, height)
{
    //猫头上半圆
    let headTopCoords = [x + width * 0.5, y + height * 0.42];
    let headTopSize = width * 0.62;
    let headTopStartAngle = Math.PI;
    let headTopEndAngle = headTopStartAngle + Math.PI;

    //猫头下半
    let headBottomCoords = [x + width * 0.5, y + height * 0.42];
    let headBottomSize = width * 0.62;
    let headBottomStartAngle = 0.0;
    let headBottomEndAngle = headBottomStartAngle + Math.PI;

    //左耳
    let leftEarTop = [x + width * 0.32, y + height * 0.13];     
    let leftEarOuter = [x + width * 0.22, y + height * 0.30];   
    let leftEarInner = [x + width * 0.40, y + height * 0.24];   

    //右耳
    let rightEarTop = [x + width * 0.68, y + height * 0.13];    
    let rightEarOuter = [x + width * 0.60, y + height * 0.24];  
    let rightEarInner = [x + width * 0.78, y + height * 0.30];  

    //左眼
    let leftEyeStart = [x + width * 0.39, y + height * 0.42];
    let leftEyeEnd = [x + width * 0.46, y + height * 0.42];

    //右眼
    let rightEyeStart = [x + width * 0.54, y + height * 0.42];
    let rightEyeEnd = [x + width * 0.61, y + height * 0.42];

    //鼻子
    let noseTop = [x + width * 0.50, y + height * 0.47];
    let noseLeft = [x + width * 0.47, y + height * 0.51];
    let noseRight = [x + width * 0.53, y + height * 0.51];

    //嘴巴
    let mouthLeftCoords = [x + width * 0.46, y + height * 0.54];
    let mouthRightCoords = [x + width * 0.54, y + height * 0.54];
    let mouthArcSize = width * 0.08;
    let mouthStartAngle = 0.0;
    let mouthEndAngle = Math.PI;

    //左胡须
    let whiskerLeftTopStart = [x + width * 0.18, y + height * 0.48];
    let whiskerLeftTopEnd = [x + width * 0.38, y + height * 0.50];

    let whiskerLeftMidStart = [x + width * 0.17, y + height * 0.54];
    let whiskerLeftMidEnd = [x + width * 0.37, y + height * 0.54];

    let whiskerLeftBotStart = [x + width * 0.18, y + height * 0.60];
    let whiskerLeftBotEnd = [x + width * 0.38, y + height * 0.58];

    //右胡须
    let whiskerRightTopStart = [x + width * 0.62, y + height * 0.50];
    let whiskerRightTopEnd = [x + width * 0.82, y + height * 0.48];

    let whiskerRightMidStart = [x + width * 0.63, y + height * 0.54];
    let whiskerRightMidEnd = [x + width * 0.83, y + height * 0.54];

    let whiskerRightBotStart = [x + width * 0.62, y + height * 0.58];
    let whiskerRightBotEnd = [x + width * 0.82, y + height * 0.60];

    p5.noFill();
    p5.stroke(255);
    p5.strokeWeight(2);

    //画猫头上半
    p5.arc(
        headTopCoords[0],
        headTopCoords[1],
        headTopSize,
        headTopSize,
        headTopStartAngle,
        headTopEndAngle
    );

    //画猫头下半
    p5.arc(
        headBottomCoords[0],
        headBottomCoords[1],
        headBottomSize,
        headBottomSize,
        headBottomStartAngle,
        headBottomEndAngle
    );

    //左耳外边线
    p5.line(leftEarOuter[0], leftEarOuter[1], leftEarTop[0], leftEarTop[1]);

    //左耳内边线
    p5.line(leftEarTop[0], leftEarTop[1], leftEarInner[0], leftEarInner[1]);

    //右耳外边线
    p5.line(rightEarOuter[0], rightEarOuter[1], rightEarTop[0], rightEarTop[1]);

    // 、、右耳内边线
    p5.line(rightEarTop[0], rightEarTop[1], rightEarInner[0], rightEarInner[1]);

    //左眼
    p5.line(leftEyeStart[0], leftEyeStart[1], leftEyeEnd[0], leftEyeEnd[1]);

    //右眼
    p5.line(rightEyeStart[0], rightEyeStart[1], rightEyeEnd[0], rightEyeEnd[1]);

    //鼻子左
    p5.line(noseTop[0], noseTop[1], noseLeft[0], noseLeft[1]);

    //鼻子右边
    p5.line(noseTop[0], noseTop[1], noseRight[0], noseRight[1]);

    //鼻子底
    p5.line(noseLeft[0], noseLeft[1], noseRight[0], noseRight[1]);

    //左嘴
    p5.arc(
        mouthLeftCoords[0],
        mouthLeftCoords[1],
        mouthArcSize,
        mouthArcSize,
        mouthStartAngle,
        mouthEndAngle
    );

    //右嘴
    p5.arc(
        mouthRightCoords[0],
        mouthRightCoords[1],
        mouthArcSize,
        mouthArcSize,
        mouthStartAngle,
        mouthEndAngle
    );

    //左上胡须
    p5.line(whiskerLeftTopStart[0], whiskerLeftTopStart[1], whiskerLeftTopEnd[0], whiskerLeftTopEnd[1]);

    //左中
    p5.line(whiskerLeftMidStart[0], whiskerLeftMidStart[1], whiskerLeftMidEnd[0], whiskerLeftMidEnd[1]);

    //左下
    p5.line(whiskerLeftBotStart[0], whiskerLeftBotStart[1], whiskerLeftBotEnd[0], whiskerLeftBotEnd[1]);

    //右上胡须
    p5.line(whiskerRightTopStart[0], whiskerRightTopStart[1], whiskerRightTopEnd[0], whiskerRightTopEnd[1]);

    //右中
    p5.line(whiskerRightMidStart[0], whiskerRightMidStart[1], whiskerRightMidEnd[0], whiskerRightMidEnd[1]);

    //右下
    p5.line(whiskerRightBotStart[0], whiskerRightBotStart[1], whiskerRightBotEnd[0], whiskerRightBotEnd[1]);
}

const drawing = p5 => {
    p5.setup = () => {
        p5.createCanvas(600, 600);
    }

    p5.draw = () => {
        p5.background(20);

        const numDrawings = 6;

        for (let i = 0; i < numDrawings; i++) {
            let size = p5.width / numDrawings;
            let xPos = size * i;

            drawCat(
                p5,
                xPos,
                (p5.height * 0.5) - (size * 0.5),
                size,
                size
            );
        }
    }
}

new p5(drawing);