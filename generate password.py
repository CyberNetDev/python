import random
import string
import hashlib

def generate_password():
    chars = string.ascii_lowercase+string.ascii_letters + string.digits +"@@@@"
    password_a = ''.join(random.choice(chars) 
    for i in range(25)).encode('utf-8')
    
    
   
  #  hash_object =hashlib.sha256(password)
   # password=hash_object.hexdigest()
    return password_a
for I in range(1,20):
    print(generate_password(),)
