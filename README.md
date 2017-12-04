# ECE16_Final

Code coming soon... 

If you want to get started early, look at https://wiki.python.org/moin/UdpCommunication 
since we will be talking to the game via UDP, locally.

The game code will be based on https://github.com/codingchili/py-race

Do not modify the main code, create your own ```controller.py``` file

The controls will be defined by the following:

- Direction: -180 to 180. Integer values, describes the angle the car is turning. 0 means the car is going in a straight line
- Gas: -1.0 to 1.0. Float values. describes the amount of gas/reverse your car is undergoing. 

When sending your controls over UDP, ensure that it is formatted as a string "direction,gas". No spaces, and in that order. Anything else **will not work**. For example, if your direction is 100, and your gas is 1.1, your message should be "100,1.1"
