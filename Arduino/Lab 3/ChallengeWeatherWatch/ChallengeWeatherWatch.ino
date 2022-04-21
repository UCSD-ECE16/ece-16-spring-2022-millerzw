void setup() {
  setupCommunication();
  setupDisplay();
}

void loop() {
  String message = receiveMessage();
  if(message != "") {
    writeDisplayCSV(message.c_str(), 2);
    sendMessage(message);
  }
}
