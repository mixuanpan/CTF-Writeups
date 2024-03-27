text_key = "trudeau" 
g = 31 
p = 97 
a = 94 
b = 21 
cipher = [131553, 993956, 964722, 1359381, 43851, 1169360, 950105, 321574, 1081658, 613914, 0, 1213211, 306957, 73085, 993956, 0, 321574, 1257062, 14617, 906254, 350808, 394659, 87702, 87702, 248489, 87702, 380042, 745467, 467744, 716233, 380042, 102319, 175404, 248489]

def generator(g, x, p):
    return pow(g, x) % p

#test_reverse 
u = generator(g, a, p) #43
v = generator(g, b, p) #8 
key = generator(v, a, p) #47 
b_key = generator(u, b, p) #47 
shared_key = key 

# len(cipher) == 34 
# reverse semi_cipher from cipher from encrypt 
# cipher = encrypt(semi_cipher, shared_key)
semi_cipher = []
for i in range(len(cipher)):
    semi_cipher.append(chr(int(cipher[i]/(47*311))))

print(semi_cipher)

# xor_encrypt_reverse
# semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
# len(text_key) == 7 ==? i % key_length: 0, 1, 2, 3, 4, 5, 6
encrypted_char_ord = []
for i in range(len(semi_cipher)): 
    encrypted_char_ord.append(ord(semi_cipher[i]))

key_char_ord = []
a = 0
while(a<len(encrypted_char_ord)):
    key_char_ord.append(ord(text_key[a%len(text_key)]))
    a += 1

backward_plaintext_ord = []
for i in range(len(encrypted_char_ord)):
    backward_plaintext_ord.append(encrypted_char_ord[i]^key_char_ord[i])
plaintext = ""
for i in range(len(backward_plaintext_ord)-1, 0, -1):
    plaintext += chr(backward_plaintext_ord[i])
    
print(plaintext) # simply add "}" at the end of the printed result 