#include <SD.h>

File myFile;
const char* myName = "Trylen"; // Replace with your name

void setup() {
  Serial.begin(9600);
  
  if (!SD.begin(4)) {
    Serial.println("SD card initialization failed!");
    return;
  }
  
  myFile = SD.open("message.txt", FILE_WRITE);
  
  if (myFile) {
    myFile.print("Hello, ");
    myFile.print(myName);
    myFile.println(".");
    myFile.println();
    myFile.println("I can count to a thousand by fives. Watch me count.");
    
    for (int i = 5; i <= 1000; i += 5) {
      myFile.println(i);
    }
    
    myFile.close();
    Serial.println("Message written to message.txt");
  } else {
    Serial.println("Error opening message.txt");
  }
}

void loop() {
  // Empty loop
}