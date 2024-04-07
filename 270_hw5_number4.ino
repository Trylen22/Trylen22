#include <SD.h>

File myFile;

void setup() {
  Serial.begin(9600);
  
  if (!SD.begin(4)) {
    Serial.println("initialization failed!");
    return;
  }
  
  myFile = SD.open("characters.txt");
  
  if (myFile) {
    char firstChar = myFile.read();
    myFile.seek(4);
    char fifthChar = myFile.read();
    myFile.seek(8);
    char ninthChar = myFile.read();
    
    myFile.close();
    
    Serial.print("First character: ");
    Serial.println(firstChar);
    Serial.print("Fifth character: ");
    Serial.println(fifthChar);
    Serial.print("Ninth character: ");
    Serial.println(ninthChar);
  } else {
    Serial.println("Error opening characters.txt");
  }
}

void loop() {
  // Empty loop
}