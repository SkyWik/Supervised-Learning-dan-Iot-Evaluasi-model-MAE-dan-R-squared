#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include "Adafruit_SHT31.h"

const char* ssid = "WIFI_SSID";
const char* password = "WIFI_PASSWORD";
const char* mqtt_server = "BROKER_IP_ADDRESS";

WiFiClient espClient;
PubSubClient client(espClient);
Adafruit_SHT31 sht31 = Adafruit_SHT31();

const int ldrPin = 34; // Pin analog untuk sensor LDR

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) { delay(500); }
  
  client.setServer(mqtt_server, 1883);
  if (!sht31.begin(0x44)) {
    Serial.println("Couldn't find SHT31");
  }
}

void loop() {
  if (!client.connected()) {
    client.connect("ESP32_Sensor_Client");
  }
  client.loop();

  float t = sht31.readTemperature();
  float h = sht31.readHumidity();
  int light = analogRead(ldrPin);

  if (!isnan(t)) {
    String payload = "{\"temperature\":" + String(t) + ", \"humidity\":" + String(h) + ", \"light\":" + String(light) + "}";
    client.publish("sensor/environment", payload.c_str());
    Serial.println("Published: " + payload);
  }
  
  delay(5000);
}
