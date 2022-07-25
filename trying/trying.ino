#include <QList.h>
#include <string>

const int in = A9;

int val;
int valmin = -1000000;
int valmax = 1000000;
int c = 0;

QList<int> list;
QList<int> temp;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  while (millis() < 100000)
  {
    val = analogRead(in);
    if (val > valmax)
    {
      valmax = val;
    }
    if (val < valmin)
    {
      valmin = val;
    }
    list.push_front(val);
    ++c;
  }
  temp = list;
  temp.pop_back();
  do
  {
   if(temp.back() == list.back())
   {
    list.pop_back();
    --c;
   }
    temp.pop_back();
  } while (temp.size() != 0);
  
}
void loop() {
  // put your main code here, to run repeatedly:
  sensorValue = analogRead(in);
  sensorValue = map(sensorValue, valmin, valmax, 0, 255);
    if (sensorValue != 0)
      Serial.println(sensorValue);
}
