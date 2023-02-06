#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

/*
    This sketch sends a string to a TCP server, and prints a one-line response.
    You must run a TCP server in your local network.
    For example, on Linux you can use this command: nc -v -l 3000
*/

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

const char* ssid     = "khaled's iphone";
const char* password = "khaled123";

const char* host = "172.20.10.5";
const uint16_t port = 7000;



ESP8266WiFiMulti WiFiMulti;

DHT dht(D1,DHT11);
WiFiClient client;

void setup() {
  Serial.begin(115200);
  // We start by connecting to a WiFi network
  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP(ssid, password);
  
  dht.begin();
  pinMode(D1,INPUT);
  
  Serial.println();
  Serial.println();
  Serial.print("Wait for WiFi... ");

  while (WiFiMulti.run() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

   
  dht.read(D1);
  
  Serial.print("connecting to ");
  Serial.print(host);
  Serial.print(':');
  Serial.println(port);

  // Use WiFiClient class to create TCP connections

  if (!client.connect(host, port)) {
    Serial.println("connection failed");
    Serial.println("wait 5 sec...");
    delay(5000);
    return;
  }

  delay(500);
}
void loop() {

  float t=dht.readTemperature();
  float h=dht.readHumidity();

  client.println("Current humidity = ");
  client.println(h);
  client.println("%  ");
  client.println("temperature = ");
  client.println(t); 
  client.println("C  ");

  Serial.println("wait 5 sec...");
  delay(5000);
  
  client.stop();

}


