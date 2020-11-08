from funcs import *
from sys import argv, stderr
from socket import socket

if len(argv) < 6:
	print("Client1:", argv[0], "<ip:port pentru server> <ip:port pentru client2> <parola> <ECB|CFB> <path>")
	exit()

server_addr = argv[1].split(":")
client2_addr = argv[2].split(":")
password = argv[3].encode('utf-8')
op_mode = argv[4]
path = argv[5]
IV = b"0123456789ABCDEF"
file = open(path, 'rb')


try:
	print("Connecting to server")
	server = socket()
	server.connect((server_addr[0], int(server_addr[1])))
except:
	print("Counld not connect to node server")
	exit()

try:
	print("Connecting to client2")
	client2 = socket()
	client2.connect((client2_addr[0], int(client2_addr[1])))
except:
	print("Counld not connect to node client2")
	exit()

# sendind op mode

client2.send(op_mode.encode("utf-8"))
server.send(op_mode.encode("utf-8"))

# decrypting the received Key

enc = server.recv(16)
client2.send(enc)
key = aes_decrypt_block(encrypted_key, K3)

if (op_mode == 'ECB'):


client2.close()
