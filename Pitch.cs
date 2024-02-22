
Random rnd = new Random();
float touchLine = rnd.Next(91, 119);
float goalLine = rnd.Next(64, 75);
float lineThickness = 0.1;
float pointThickness =0.25;

float horizontalRotate = new Vector(0, 0, 0);
float verticalRotate = new Vector(90, 0, 0);
float spaceRotate = new Vector(0, 90, 0);

float crossbar = 7.32;
float sidebar = 2.44;

float goalAreaTop = 18.29;
float goalAreaSide = 5.23;

float penaltyAreaTop = 40.23;
float penaltyAreaSide = 16.46;

float penaltyPoint = 10.97;

float centerCircleRadius = 9.14;

float halfLine = goalLine;
float penaltyArc = 9.14;

//gólvonal
GameObject goalLineObj1 = GameObject.CreatePrimitive(PrimitiveType.Cube);
goalLineObj1.transform.position = new Vector3(-goalLine / 2, 0, -goalLine / 2);
goalLineObj1.transform.rotate = verticalRotate;
goalLineObj1.transform.scale = new Vector3(goalLine, 0.1, lineThickness);

GameObject goalLineObj2 = GameObject.CreatePrimitive(PrimitiveType.Cube);
goalLineObj2.transform.position = new Vector3(touchLine - goalLine / 2, 0, -goalLine / 2);
goalLineObj2.transform.rotate = verticalRotate;
goalLineObj2.transform.scale = new Vector3(goalLine, 0.1, lineThickness);


//oldalvonal
GameObject touchLine1 = GameObject.CreatePrimitive(PrimitiveType.Cube);
touchLine1.transform.position = new Vector3(touchLine / 2, 0, 0);
touchLine1.transform.rotate = new Vector3(0, 0, 0);
touchLine1.transform.scale = new Vector3(touchLine, 0.1, lineThickness);

GameObject touchLine2 = GameObject.CreatePrimitive(PrimitiveType.Cube);
touchLine2.transform.position = new Vector3(touchLine / 2, 0, -goalLine);
touchLine2.transform.rotate = new Vector3(0, 0, 0);
touchLine2.transform.scale = new Vector3(touchLine, 0.1, lineThickness);

//félpálya vonal
GameObject halfLine = GameObject.CreatePrimitive(PrimitiveType.Cube);
halfLine.transform.position = new Vector3(0, 0, -goalLine / 2);
halfLine.transform.rotate = verticalRotate;
halfLine.transform.scale = new Vector3(goalLine, 0.1, lineThickness);

//saját 16-os
GameObject penaltyAreaTopObj = GameObject.CreatePrimitive(PrimitiveType.Cube);
penaltyAreaTopObj.transform.position = new Vector3(touchLine - penaltyAreaSide - penaltyAreaSide / 2, 0, goalLine / 2);
penaltyAreaTopObj.transform.rotate = verticalRotate;
penaltyAreaTopObj.transform.scale = new Vector3(penaltyAreaTop, 0.1, lineThickness);

GameObject penaltyAreaSide1Obj = GameObject.CreatePrimitive(PrimitiveType.Cube);
penaltyAreaSide1Obj.transform.position = new Vector3(touchLine - penaltyAreaSide / 2, 0, goalLine / 2 + penaltyAreaTop / 2);
penaltyAreaSide1Obj.transform.rotate = horizontalRotate;
penaltyAreaSide1Obj.transform.scale = new Vector3(penaltyAreaSide, 0.1, lineThickness);

GameObject penaltyAreaSide2Obj = GameObject.CreatePrimitive(PrimitiveType.Cube);
penaltyAreaSide2Obj.transform.position = new Vector3(touchLine - penaltyAreaSide / 2, 0, goalLine / 2 - penaltyAreaTop / 2);
penaltyAreaSide2Obj.transform.rotate = horizontalRotate;
penaltyAreaSide2Obj.transform.scale = new Vector3(penaltyAreaSide, 0.1, lineThickness);

//saját ötös
GameObject goalAreaTopObj = GameObject.CreatePrimitive(PrimitiveType.Cube);
goalAreaTopObj.transform.position = new Vector3(touchLine - goalAreaSide - goalAreaSide / 2, 0, goalLine / 2);
goalAreaTopObj.transform.rotate = verticalRotate;
goalAreaTopObj.transform.scale = new Vector3(goalAreaTop, 0.1, lineThickness);

GameObject goalAreaSide1Obj = GameObject.CreatePrimitive(PrimitiveType.Cube);
goalAreaSide1Obj.transform.position = new Vector3(touchLine - goalAreaSide / 2, 0, goalLine / 2 + goalAreaTop / 2);
goalAreaSide1Obj.transform.rotate = horizontalRotate;
goalAreaSide1Obj.transform.scale = new Vector3(goalAreaSide, 0.1, lineThickness);

GameObject goalAreaSide2Obj = GameObject.CreatePrimitive(PrimitiveType.Cube);
goalAreaSide2Obj.transform.position = new Vector3(touchLine - goalAreaSide / 2, 0, goalLine / 2 - goalAreaTop / 2);
goalAreaSide2Obj.transform.rotate = horizontalRotate;
goalAreaSide2Obj.transform.scale = new Vector3(goalAreaSide, 0.1, lineThickness);

//ellenfél tizenhatosa
GameObject penaltyAreaTopRObj = GameObject.CreatePrimitive(PrimitiveType.Cube);
penaltyAreaTopRObj.transform.position = new Vector3(penaltyAreaSide / 2, 0, goalLine / 2);
penaltyAreaTopRObj.transform.rotate = verticalRotate;
penaltyAreaTopRObj.transform.scale = new Vector3(penaltyAreaTop, 0.1, lineThickness);


GameObject penaltyAreaSide1RObj = GameObject.CreatePrimitive(PrimitiveType.Cube);
penaltyAreaSide1RObj.transform.position = new Vector3(penaltyAreaSide / 2, 0, goalLine / 2 + penaltyAreaTop / 2);
penaltyAreaSide1RObj.transform.rotate = horizontalRotate;
penaltyAreaSide1RObj.transform.scale = new Vector3(penaltyAreaSide, 0.1, lineThickness);

GameObject penaltyAreaSide2RObj = GameObject.CreatePrimitive(PrimitiveType.Cube);
penaltyAreaSide2RObj.transform.position = new Vector3(penaltyAreaSide / 2, 0, goalLine / 2 - penaltyAreaTop / 2);
penaltyAreaSide2RObj.transform.rotate = horizontalRotate;
penaltyAreaSide2RObj.transform.scale = new Vector3(goalAreaSide, 0.1, lineThickness);

//ellenfél ötöse
GameObject goalAreaTopRObj = GameObject.CreatePrimitive(PrimitiveType.Cube);
goalAreaTopRObj.transform.position = new Vector3(goalAreaSide / 2, 0, goalLine / 2);
goalAreaTopRObj.transform.rotate = verticalRotate;
goalAreaTopRObj.transform.scale = new Vector3(goalAreaTop, 0.1, lineThickness);

GameObject goalAreaSide1RObj = GameObject.CreatePrimitive(PrimitiveType.Cube);
goalAreaSide1RObj.transform.position = new Vector3(goalAreaSide / 2, 0, goalLine / 2 + goalAreaTop / 2);
goalAreaSide1RObj.transform.rotate = horizontalRotate;
goalAreaSide1RObj.transform.scale = new Vector3(goalAreaSide, 0.1, lineThickness);

GameObject goalAreaSide2RObj = GameObject.CreatePrimitive(PrimitiveType.Cube);
goalAreaSide2RObj.transform.position = new Vector3(goalAreaSide / 2, 0, goalLine / 2 - goalAreaTop / 2);
goalAreaSide2RObj.transform.rotate = horizontalRotate;
goalAreaSide2RObj.transform.scale = new Vector3(goalAreaSide, 0.1, lineThickness);



//saját kapu
GameObject crossbarObj = GameObject.CreatePrimitive(PrimitiveType.Cube);
crossbarObj.transform.position = new Vector3(touchLine - crossbar / 2, sidebar, goalLine / 2);
crossbarObj.transform.rotate = verticalRotate;
crossbarObj.transform.scale = new Vector3(crossbar, 0.1, lineThickness);

GameObject sidebar1Obj = GameObject.CreatePrimitive(PrimitiveType.Cube);
sidebar1Obj.transform.position = new Vector3(touchLine - sidebar / 2, 0, goalLine / 2 - crossbar / 2);
sidebar1Obj.transform.rotate = spaceRotate;
sidebar1Obj.transform.scale = new Vector3(sidebar, 0.1, lineThickness);

GameObject sidebar2Obj = GameObject.CreatePrimitive(PrimitiveType.Cube);
sidebar2Obj.transform.position = new Vector3(touchLine, 0, goalLine / 2 + crossbar / 2);
sidebar2Obj.transform.rotate = spaceRotate;
sidebar2Obj.transform.scale = new Vector3(sidebar, 0.1, lineThickness);

// ellenfél kapuja 
GameObject crossbarRObj = GameObject.CreatePrimitive(PrimitiveType.Cube);
crossbarRObj.transform.position = new Vector3(-crossbar / 2, sidebar, goalLine / 2);
crossbarRObj.transform.rotate = verticalRotate;
crossbarRObj.transform.scale = new Vector3(crossbar, 0.1, lineThickness);

GameObject sidebar1RObj = GameObject.CreatePrimitive(PrimitiveType.Cube);
sidebar1RObj.transform.position = new Vector3(-sidebar / 2, 0, goalLine / 2 - crossbar / 2);
sidebar1RObj.transform.rotate = spaceRotate;
sidebar1RObj.transform.scale = new Vector3(sidebar, 0.1, lineThickness);


GameObject sidebar2RObj = GameObject.CreatePrimitive(PrimitiveType.Cube);
sidebar2RObj.transform.position = new Vector3(-sidebar / 2, 0, goalLine / 2 + crossbar / 2);
sidebar2RObj.transform.rotate = spaceRotate;
sidebar2RObj.transform.scale = new Vector3(sidebar, 0.1, lineThickness);


//saját büntetőpont
GameObject penaltyPointObj = GameObject.CreatePrimitive(PrimitiveType.Sphere);
penaltyPointObj.transform.position = new Vector3(touchLine - penaltyPoint, 0, goalLine / 2);
penaltyPointObj.transform.scale = new Vector3(pointThickness, pointThickness, pointThickness);

//ellenfél büntetőpont
GameObject penaltyPointRObj = GameObject.CreatePrimitive(PrimitiveType.Sphere);
penaltyPointRObj.transform.position = new Vector3(penaltyPoint, 0, goalLine / 2);
penaltyPointRObj.transform.scale = new Vector3(pointThickness, pointThickness, pointThickness);
