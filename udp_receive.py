import socket
import select

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(0.00001)
sock.setblocking(False)

while True:
    ready = select.select([sock], [], [], 0.0)
    if (ready[0]):
        data, addr = sock.recvfrom(1024)
        message = data.decode()
        print("Received message:", message)

        message_arr = message.split(",")

        direction = int(message_arr[0])
        gas = float(message_arr[1])

        print("Direction: ", direction)
        print("Gas: ", gas)
