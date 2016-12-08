//
//   FILE:  dht_test.pde
// PURPOSE: DHT library test sketch for Arduino
//

#include "dht.h"
#include <stdio.h>
#include <unistd.h>
dht DHT;

#define DHT11_PIN 4//put the sensor in the digital pin 4

int main()
{
	while (1)
	{
		wiringPiSetup ();
		int chk = DHT.read11(DHT11_PIN);
		if (chk == 0)
		{
			printf("%f\n", DHT.humidity);
			printf("%f\n", DHT.temperature);
		}
		sleep(1);
	}
}
