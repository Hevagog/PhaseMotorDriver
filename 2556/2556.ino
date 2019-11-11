char data[256][6];


void setup(){
  Serial.begin(115200);
  
  pinMode(2 , INPUT);
  pinMode(3 , INPUT);
  pinMode(4 , INPUT);

  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
}


void loop(){
  for(int i = 0; i < 256; i++){
    data[i][0] = 0;

    if(digitalRead(2)){
      data[i][0]++;
    }
    data[i][0] << 1;
    if(digitalRead(3)){
      data[i][0]++;
    }
    data[i][0] << 1;
    if(digitalRead(4)){
      data[i][0]++;
    }

    int a1 = analogRead(A1);
    int a2 = analogRead(A2);
    int a3 = analogRead(A3);
    int time = millis();

    data[i][0] += a1 << 3;
    data[i][1] += a1 >> 5;
    data[i][1] += a2 << 7;
    data[i][2] += a2 >> 3;
    data[i][2] += a3 << 9;
    data[i][3] += a3 >> 1;
    data[i][4] += a3 >> 9;
    data[i][4] += time << 1;
    data[i][5] += time >> 7;


    
  }
  for(int i = 0; i < 256; i++){
    for(int n = 0 ; n < 6 ; n ++){
      Serial.write(data[i][n]);
    }
    
  }
}
