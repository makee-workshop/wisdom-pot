void setup() {
  
  Serial.begin(9600);
}

void loop() {
  uint8_t a = 0; 
  int b = 0;
  enableChar();
  
  delay(500);
}

String  enableChar(){
  
  char c = 0;
  String buffer = "";
  
  while((c= Serial.read())>0){
    String cs = String(c);
    buffer = buffer + cs;
   
  }
  if(buffer!=""){
    Serial.println(buffer);
  }
  return buffer;
}
String enableString(){
  Serial.println("loop");
  String buf= Serial.readString();
  Serial.println(buf);
}
