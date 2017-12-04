import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

direction = 50  # Direction, int
gas = 1.5  # Gas, float


# Requirement: String must be formatted as "direction,gas"
# Anything else will not work. In this example, it would be "50,1.5"
MESSAGE = ("%s,%s" % (direction,gas))


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create the socket
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))  # Send the message

