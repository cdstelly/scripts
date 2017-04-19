#include <iostream>
#include <stdint.h>
using namespace std;

#define     SYNC_BIT_VALUE  0
#define     SYNC_PULSE_MIN  1
#define     SYNC_PULSE_DEF  3
#define     SYNC_PULSE_MAX  5
#define DECOUPLING_MASK 0b11001010 

void sendZero() {
    cout << "zero" << endl;
    
}

void sendOne() {
    cout << "one" << endl;
}

void transmitArray(uint8_t numBytes, uint8_t *data){

#if SYNC_BIT_VALUE
  for( int8_t i = 0; i < SYNC_PULSE_DEF; i++) //send capture pulses
  {
    sendOne(); //end of capture pulses
  }
  sendZero(); //start data pulse
#else
  for( int8_t i = 0; i < SYNC_PULSE_DEF; i++) //send capture pulses
  {
    sendZero(); //end of capture pulses
  }
  sendOne(); //start data pulse
#endif
 
  // Send the user data
  for (uint8_t i = 0; i < numBytes; i++)
  {
    uint16_t mask = 0x01; //mask to send bits
    uint8_t d = data[i] ^ DECOUPLING_MASK;
    for (uint8_t j = 0; j < 8; j++)
    {
      if ((d & mask) == 0)
        sendZero();
      else
        sendOne();
      mask <<= 1; //get next bit
    }//end of byte
  }//end of data

// Send 3 terminatings 0's to correctly terminate the previous bit and to turn the transmitter off
#if SYNC_BIT_VALUE
  sendOne();
  sendOne();
  sendOne();
#else
  sendZero();
  sendZero();
  sendZero();
#endif
}//end of send the data


int main() {
	uint16_t data = '1';
	uint8_t byteData[2] = {data >> 8, data & 0xFF};
	transmitArray(2, byteData);
	return 0;
}
