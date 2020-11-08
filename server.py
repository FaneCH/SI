from funcs import *
from sys import argv
from socket import socket

if len(argv) < 3:
	print("Server:", argv[0], "<ip:port pentru server> <parola>")
	exit()

ip, port = argv[1].split(":")
password = argv[2].encode('utf-8')

Key = get_random_bytes(16)

def send_data(client, ip_port):
	ip_port = ip_port[0] + ":" + str(ip_port[1])
	print("New client", ip_port)
	Enc_mode = client.recv(3)
	K = ecb_encrypt(K, K_p, 16)
	if Enc_mode == 'ECB':
		K = ecb_encrypt(K, K_p, 16)
	elif Enc_mode == 'CFB':
		iv = get.get_random_bytes(16)
		K = cfb_encrypt(K, K_p, 16, iv)
	client.send(encrypt_block(Key, password))
	client.close()

try:
	create_server(ip, port, send_data)
except Exception as e:
	print("Server is closing")
