//ver 0.001
char data[1536];

void setup() {
  Serial.begin(1000000);
  // put your setup code here, to run once:
for(int i = 0; i < 256; i++){
  data[(6*i) + 0] = i;
  data[(6*i) + 1] = i;
  data[(6*i) + 2] = i;
  data[(6*i) + 3] = i;
  data[(6*i) + 4] = i;
  data[(6*i) + 5] = i;

  }
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(1000);
Serial.write(data , 1536);
}
