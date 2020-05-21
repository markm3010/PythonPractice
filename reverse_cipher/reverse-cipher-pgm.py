# Reverse Cipher

message = 'those days are gone,these new days are here.nobody likes it but at least I have beer'

msg_len = len(message) - 1

encrypted_msg = ''
while msg_len >=0:
    encrypted_msg += message[msg_len]
    msg_len -= 1

print(f"UNENCRYPTED MESSAGE:\n>>>{message}<<<\n")
print(f"ENCRYPTED MESSAGE:\n>>>{encrypted_msg}<<<\n")
