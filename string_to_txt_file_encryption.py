# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64

import random, string
def randomword(length):
   letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
   return ''.join(random.choice(letters) for i in range(length))

secret_key = '1234567890123456' # create new & store somewhere safe
cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously

if (False):
    input_txt = 'test some plain text here'

    msg_text = input_txt.rjust(64)
    
    encoded = base64.b64encode(cipher.encrypt(msg_text))
    
    decoded = cipher.decrypt(base64.b64decode(encoded))
    
    print("Secret message is : ", input_txt)
    print('Secret Key is : ', secret_key)
    print('-'*60)
    print('Encrypted message is : ', encoded)
    print('-'*60)
    print('DeCrypted message is : ', decoded)
    print('Pretty print DeCrypted message : ', decoded.strip().decode("utf-8"))
    print('-'*60)

#----------------------------------------

secret_key16 = '1234567890123456'
secret_key24 = '123456789012345612345678'
secret_key32 = '12345678901234561234567890123456'

secret_key = randomword(32)


cipher = AES.new(secret_key,AES.MODE_ECB) 

#convert to bytes
#usr = "This is a test" 
#usr = b"user_ID\n" #or usr = "user_ID\n".encode()
input_string = "user_ID"
usr = input_string + "\n"
usr = usr.rjust(16)
usr = usr.encode()
print(usr)

encoded = base64.b64encode(cipher.encrypt(usr))

#save to txt file
with open("my_text.txt", "wb") as f:
    #f.write(usr)
    f.write(encoded)
    f.close()
#in_file = open("my_text.txt", "rb") # opening for [r]eading as [b]inary
#data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
#in_file.close()

#open txt file
with open("my_text.txt", "rb") as f:
    content = f.readlines()
    f.close()
content = [x.strip() for x in content] 
print(content)

#str(content[0])[2:9]
decoded = cipher.decrypt(base64.b64decode(content[0]))
output_string = str(decoded.strip())[2:-1]
print(output_string)
