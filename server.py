import socket

def udp_server():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    print('UDP server is listening on {}:{}'.format(*server_address))

    while True:
        # Receive data from the client
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode('utf-8')

        print('Received message from {}: {}'.format(client_address, message))

        # Check if the client wants to exit
        if message.lower() == 'exit':
            print('Client requested exit. Closing connection.')
            break

        # Send a reply back to the client
        reply_message = 'Server received: {}'.format(message)
        server_socket.sendto(reply_message.encode('utf-8'), client_address)

    # Close the socket
    server_socket.close()

if __name__ == '__main__':
    udp_server()
