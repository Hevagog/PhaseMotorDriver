//version 0.002
char data[1536];

union {
   unsigned long var;
   char chars[4];
}u;


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
  for(int i = 0; i < 256; i++){
    data[i* 6] = char(0);

    if(digitalRead(2)){
      data[i* 6]++;
    }
    data[i* 6] << 1;
    if(digitalRead(3)){
      data[i* 6]++;
    }
    data[i* 6] << 1;
    if(digitalRead(4)){
      data[i* 6]++;
    }

    unsigned int a1 = analogRead(A1);
    //a1 >> 2;
    data[(i * 6) + 1] = char(a1);
    
    unsigned int a2 = analogRead(A2);
    //a2 >> 2;
    data[(i * 6) + 2] = char(a2);
    
    unsigned int a3 = analogRead(A3);
    //a3 >> 2;
    data[(i * 6) + 3] = char(a3);
   

    //u.var = millis();
    u.var = 10000;
    data[(i * 6) + 4] = u.chars[1];
    data[(i * 6) + 5] = u.chars[0];

    


    
  }

      Serial.write(data , 1536);
      //delay(10000);
      //Serial.flush();

}
