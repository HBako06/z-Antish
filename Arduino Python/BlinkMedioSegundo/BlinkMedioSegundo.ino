// Definimos el pin del LED
int ledPin = 13;

// Configuramos el pin como salida
void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

// Hacemos parpadear el LED
void loop() {
  Serial.println("--Prendido!");
  digitalWrite(ledPin, HIGH); // encendemos el LED
  delay(500); // esperamos medio segundo
  digitalWrite(ledPin, LOW); // apagamos el LED
  Serial.println("Apagado!");
  delay(500); // esperamos medio segundo
}
