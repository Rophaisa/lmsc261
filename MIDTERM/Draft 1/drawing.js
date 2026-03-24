const drawing = p5 => {

    p5.setup = () => {

        p5.createCanvas(600, 600); //大小
    }

    p5.draw = () => {
        p5.background(20);// 颜色（背景）

        //head arcs 上半圆
        let headTopCoords = [p5.width * 0.5, p5.height * 0.42];
        let headTopSize = p5.width * 0.62;
        let headTopStartAngle = Math.PI;
        let headTopEndAngle = headTopStartAngle + Math.PI;
        //下半个
        let headBottomCoords = [p5.width * 0.5, p5.height * 0.42];
        let headBottomSize = p5.width * 0.62;
        let headBottomStartAngle = 0.0;
        let headBottomEndAngle = headBottomStartAngle + Math.PI;

        //left ear 三角
        let leftEarTop = [p5.width * 0.32, p5.height * 0.13];
        let leftEarOuter = [p5.width * 0.22, p5.height * 0.30];
        let leftEarInner = [p5.width * 0.40, p5.height * 0.24];

        //right
        let rightEarTop = [p5.width * 0.68, p5.height * 0.13];
        let rightEarOuter = [p5.width * 0.60, p5.height * 0.24];
        let rightEarInner = [p5.width * 0.78, p5.height * 0.30];

        //左眼
        let leftEyeStart = [p5.width * 0.39, p5.height * 0.42];
        let leftEyeEnd = [p5.width * 0.46, p5.height * 0.42];
        //right
        let rightEyeStart = [p5.width * 0.54, p5.height * 0.42];
        let rightEyeEnd = [p5.width * 0.61, p5.height * 0.42];

        // nose
        let noseTop = [p5.width * 0.50, p5.height * 0.47];
        let noseLeft = [p5.width * 0.47, p5.height * 0.51];
        let noseRight = [p5.width * 0.53, p5.height * 0.51];

        // mouth arcs
        let mouthLeftCoords = [p5.width * 0.46, p5.height * 0.54];
        let mouthRightCoords = [p5.width * 0.54, p5.height * 0.54];
        let mouthArcSize = p5.width * 0.08;
        let mouthStartAngle = 0.0;
        let mouthEndAngle = Math.PI;

        // whiskers left
        let whiskerLeftTopStart = [p5.width * 0.18, p5.height * 0.48];
        let whiskerLeftTopEnd = [p5.width * 0.38, p5.height * 0.50];

        let whiskerLeftMidStart = [p5.width * 0.17, p5.height * 0.54];
        let whiskerLeftMidEnd = [p5.width * 0.37, p5.height * 0.54];

        let whiskerLeftBotStart = [p5.width * 0.18, p5.height * 0.60];
        let whiskerLeftBotEnd = [p5.width * 0.38, p5.height * 0.58];
//rigght
        let whiskerRightTopStart = [p5.width * 0.62, p5.height * 0.50];
        let whiskerRightTopEnd = [p5.width * 0.82, p5.height * 0.48];

        let whiskerRightMidStart = [p5.width * 0.63, p5.height * 0.54];
        let whiskerRightMidEnd = [p5.width * 0.83, p5.height * 0.54];

        let whiskerRightBotStart = [p5.width * 0.62, p5.height * 0.58];
        let whiskerRightBotEnd = [p5.width * 0.82, p5.height * 0.60];

        p5.noFill();
        p5.stroke(255);
        p5.strokeWeight(3);

        // draw head
        p5.arc(
            headTopCoords[0],
            headTopCoords[1],
            headTopSize,
            headTopSize,
            headTopStartAngle,
            headTopEndAngle
        );
//下半个
        p5.arc(
            headBottomCoords[0],
            headBottomCoords[1],
            headBottomSize,
            headBottomSize,
            headBottomStartAngle,
            headBottomEndAngle
        );

        //left ear
        p5.line(leftEarOuter[0], leftEarOuter[1], leftEarTop[0], leftEarTop[1]);
        p5.line(leftEarTop[0], leftEarTop[1], leftEarInner[0], leftEarInner[1]);

        //right
        p5.line(rightEarOuter[0], rightEarOuter[1], rightEarTop[0], rightEarTop[1]);
        p5.line(rightEarTop[0], rightEarTop[1], rightEarInner[0], rightEarInner[1]);

        //Eyes
        p5.line(leftEyeStart[0], leftEyeStart[1], leftEyeEnd[0], leftEyeEnd[1]);
        p5.line(rightEyeStart[0], rightEyeStart[1], rightEyeEnd[0], rightEyeEnd[1]);

        //nose
        p5.line(noseTop[0], noseTop[1], noseLeft[0], noseLeft[1]);
        p5.line(noseTop[0], noseTop[1], noseRight[0], noseRight[1]);
        p5.line(noseLeft[0], noseLeft[1], noseRight[0], noseRight[1]);

        //mouth
        p5.arc(
            mouthLeftCoords[0],
            mouthLeftCoords[1],
            mouthArcSize,
            mouthArcSize,
            mouthStartAngle,
            mouthEndAngle
        );

        p5.arc(
            mouthRightCoords[0],
            mouthRightCoords[1],
            mouthArcSize,
            mouthArcSize,
            mouthStartAngle,
            mouthEndAngle
        );



        // draw whiskers
        //左上
        p5.line(whiskerLeftTopStart[0], whiskerLeftTopStart[1], whiskerLeftTopEnd[0], whiskerLeftTopEnd[1]);
        //左中
        p5.line(whiskerLeftMidStart[0], whiskerLeftMidStart[1], whiskerLeftMidEnd[0], whiskerLeftMidEnd[1]);
        //下
        p5.line(whiskerLeftBotStart[0], whiskerLeftBotStart[1], whiskerLeftBotEnd[0], whiskerLeftBotEnd[1]);
        //右上
        p5.line(whiskerRightTopStart[0], whiskerRightTopStart[1], whiskerRightTopEnd[0], whiskerRightTopEnd[1]);
        //中
        p5.line(whiskerRightMidStart[0], whiskerRightMidStart[1], whiskerRightMidEnd[0], whiskerRightMidEnd[1]);
        //bottom
        p5.line(whiskerRightBotStart[0], whiskerRightBotStart[1], whiskerRightBotEnd[0], whiskerRightBotEnd[1]);
    }
}



new p5(drawing);


