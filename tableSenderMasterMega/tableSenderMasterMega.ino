//version 0.001.Mega
char data[1792];

unsigned long timeStamp;

union {
   unsigned long var;
   char chars[4];
}u;
int x;
void setup(){
  Serial.begin(1000000);

  attachInterrupt(digitalPinToInterrupt(2), zaWarudo, RISING);

  pinMode(8, INPUT);
  pinMode(9, OUTPUT);
  
  pinMode(5 , INPUT);
  pinMode(6 , INPUT);
  pinMode(7 , INPUT);

  pinMode(A1, INPUT_PULLUP);
  pinMode(A2, INPUT_PULLUP);
  pinMode(A3, INPUT_PULLUP);

  pinMode(12,INPUT);
  
  digitalWrite(9, LOW);
}

void zaWarudo(){
  if(digitalRead(12)){

    timeStamp = millis();
    }
  }

void loop(){


  
  while(digitalRead(8) == HIGH){
    digitalWrite(13 , HIGH);
  }
  digitalWrite(13 , LOW);
  digitalWrite(9 , HIGH);
  
    for(int i = 0; i < 256; i++){
      data[i* 7 + 1] = char(1);

      if(digitalRead(5)){
        data[i* 7 + 1]+=2;
      }
      if(digitalRead(6)){
        data[i* 7 + 1]+=4;
      }
      if(digitalRead(7)){
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
   

      u.var = millis()-timeStamp;
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
    
    digitalWrite(9 , LOW);
        Serial.write(data , 1792);
       
  

}
