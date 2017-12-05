# ECE16_Final

Install the ```pygame``` library prior to working with the code

Utilizing EMG data from each arm, as well as gyro and accel data, create a game controller to control the car in py-race.

We will be using UDP to communicate to our game. Look at ```udp_receive.py``` and ```udp_send.py``` as examples.

The game code will be based on https://github.com/codingchili/py-race

Do not modify the main code, create your own ```controller.py``` file. You should use the same code as ```udp_send.py``` to talk to the main code via UDP.

The controls will be defined by the following:

- Direction: -180 to 180. Integer values, describes the angle the car is turning. 0 means the car is going in a straight line
- Gas: -1.0 to 1.0. Float values. describes the amount of gas/reverse your car is undergoing. 

When sending your controls over UDP, ensure that it is formatted as a string "direction,gas". No spaces, and in that order. Anything else **will not work**. For example, if your direction is 100, and your gas is 1.1, your message should be "100,1.1"
