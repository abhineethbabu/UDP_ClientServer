import socket

def udp_client():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Server address and port
    server_address = ('localhost', 12345)

    while True:
        # Get user input
        message = input('Enter a message (type "exit" to quit): ')

        # Send the message to the server
        client_socket.sendto(message.encode('utf-8'), server_address)

        # Receive the reply from the server
        data, server_address = client_socket.recvfrom(1024)
        reply_message = data.decode('utf-8')

        print('Received reply from {}: {}'.format(server_address, reply_message))

        # Check if the user wants to exit
        if message.lower() == 'exit':
            print('Closing connection.')
            break

    # Close the socket
    client_socket.close()

if __name__ == '__main__':
    udp_client()
