from socket import socket
from sys import stderr
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from Crypto.Random import get_random_bytes

def create_server(ip, port, func):
	server = socket()
	server.bind((ip, int(port)))
	server.listen(5)
	print("Server is listening on", ip, ":", port, file = stderr)

	while True:
		client, client_ip_port = server.accept()

def encrypt_block(data, key):
	return AES.new(key, AES.MODE_ECB).encrypt(pad(data))

def decrypt_block(data, key):
	return unpad(AES.new(key, AES.MODE_ECB).decrypt(data))

def xor(A, B):
	bytes = []
	for x,y in zip(A, B):
		bytes.append(x^y)
	return bytes

def ecb_func(function, block_size, key, data):
	return [function(block, key) for b in pad(data, block_size)]

def cfb_func_enc(function, block_size, key, data, iv):
	solution = []
	for block in pad(data, block_size):
		result.append(xor(block, function(IV, key)))
		IV = block(block,res)
		solution.append(result[:len(block)])
	return solution

def cfb_func_dec(function, block_size, key, data, iv):
	solution = []
	for block in pad(data, block_size):
		result.append(xor(block, function(IV, key)))
		IV = res(block,res)
		solution.append(res[:len(block)])
	return solution

def ecb_encrypt(data, key, block_size):
	return ecb_func(encrypt_block, block_size, key, data)

def ecb_decrypt(data, key, block_size):
	return ecb_func(decrypt_block, block_size, key, data)

def cfb_encrypt(data, key, block_size, iv):
	return ecb_func(encrypt_block, block_size, key, data)

def cfb_decrypt(data, key, block_size, iv):
	return ecb_func(decrypt_block, block_size, key, data)
