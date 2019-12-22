//version 0.001
char data[1792];

union {
   unsigned long var;
   char chars[4];
}u;

//int c;
void setup(){
  Serial.begin(1000000);
  
  pinMode(2 , INPUT);
  pinMode(3 , INPUT);
  pinMode(4 , INPUT);

  pinMode(A1, INPUT_PULLUP);
  pinMode(A2, INPUT_PULLUP);
  pinMode(A3, INPUT_PULLUP);
}


void loop(){
  //c =digitalRead(2);
   //   Serial.print(c);
  for(int i = 0; i < 256; i++){
    data[i* 7 + 1] = char(1);

    if(digitalRead(2)){
      data[i* 7 + 1]+=2;
    }
    if(digitalRead(3)){
      data[i* 7 + 1]+=4;
    }
    if(digitalRead(4)){
      data[i* 7 + 1]+=8;
    }
    

    unsigned int a1 = analogRead(A1) + 1;
    //a1 >> 2;
    data[(i * 7) + 2] = char(a1);
    
    unsigned int a2 = analogRead(A2) + 1;
    //a2 >> 2;
    data[(i * 7) + 3] = char(a2);
    
    unsigned int a3 = analogRead(A3) + 1;
    //a3 >> 2;
    data[(i * 7) + 6] = char(a3);
   

    u.var = millis()+1;
    //u.var = 10000;
    data[(i * 7) + 4] = u.chars[1];
    data[(i * 7) + 5] = u.chars[0];
//    Serial.print("CHARS - ");
//    Serial.print(u.chars[1]); Serial.print("  ");
//    Serial.print(u.chars[0]);
//    Serial.println("");
    
//    for (int q;q<6;q++){
//        data[(i*7) + 6] += data[(i*7) + q];
//        }
    data[i*7] = 0;
  }

      Serial.write(data , 1792);
      //delay(10000);
      //Serial.flush();

}
