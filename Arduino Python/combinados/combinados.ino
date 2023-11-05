int ledPin = 13;
char command;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600); // Inicia la comunicación por puerto serie
}

void loop() {
  if (Serial.available() > 0)
  {
    // Lee el comando y lo guarda en una variable
    command = Serial.read();

    // Si el comando es "BlinkMedioSegundo", cambia al proyecto BlinkMedioSegundo
    if (command == '1') {
      while(true){
        digitalWrite(ledPin, HIGH); // encendemos el LED
        delay(1000);
        digitalWrite(ledPin, LOW);
        delay(1000);

        // Verifica si se ha recibido el comando para detener el bucle
        if (Serial.available() > 0) {
          command = Serial.read();
          if (command == '0') {
            break;
          }
        }
      }
    }
    if (command == 'A') { 
      digitalWrite(ledPin, HIGH); // apagamos el LED
    }
    if (command == 'B') { 
      digitalWrite(ledPin, LOW); // apagamos el LED
    }
  }
}