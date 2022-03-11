from utils import my_func
import os
import sys

def encrypt():
    print("\nBrowse your video file to encrypt")
    file_Name, new_Filename = my_func.newFileOrNot('Encrypted')
    encryption = my_func.ciphering()
    mykey = encryption.create_secret_key()
    encryption.write_secret_key(mykey, os.getcwd()+"/"+'secret.key')
    loaded_key = encryption.load_secret_key(os.getcwd()+"/"+'secret.key')
    encryption.encrypt_file(loaded_key, file_Name, new_Filename)
    print("File Encrypted..")
    sys.exit("Sucess !!")