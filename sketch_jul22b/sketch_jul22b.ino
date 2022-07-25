#include <Queue>

const int in = A9;

int val = 0;
int valmin = -1000000;
int valmax = 1000000;
int c = 1;

Queue list(sizeof(int), 1000, FIFO, false);
Queue unique(sizeof(int), 1000, FIFO, false);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  while (millis() < 100000)
  {
    val = analogRead(in);
    if (val > valmax)
      valmax = val;
    if (val < valmin)
      valmin = val;
    list.push(val);
  }
  do
  {
   for (int x = 0; x < list.sizeOf(); ++x)
   {
    unique.push(list.front);
    Serial.println("pushing " << list.peak)
    queue<int>temp = unique;
    while(temp.sizeOf() != 0)
    {
      temp.pop();
      if (temp.front == unique.front)
        unique.pop();
    }
   }
    
  } while (list.sizeOf() != 0);
}

void loop() {
  // put your main code here, to run repeatedly:

}
