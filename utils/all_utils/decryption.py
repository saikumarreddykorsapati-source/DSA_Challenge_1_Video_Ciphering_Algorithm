from utils import my_func
import os
import sys

def decrypt():
    try:
        print("Browse your video file to decrypt")
        file_Name, new_Filename = my_func.newFileOrNot('Decrypted')
        decryption=my_func.ciphering()
        loaded_key=decryption.load_secret_key(os.getcwd()+"/"+'secret.key')
        decryption.decrypt_file(loaded_key, file_Name, new_Filename)
        print("File Decrypted...")
        sys.exit("Sucess !!")

    except Exception as e:
        print("Error Occured :",e)
        sys.exit("Sorry !!")

