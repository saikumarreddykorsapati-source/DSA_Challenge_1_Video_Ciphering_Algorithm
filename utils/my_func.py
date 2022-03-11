from cryptography.fernet import Fernet
from tkinter import *
from tkinter import filedialog
import os
import sys

class ciphering():

    def create_secret_key(self):
        secret_key = Fernet.generate_key()
        return secret_key

    def write_secret_key(self, secret_key, kname):
        with open(kname, 'wb') as confidentialkey:
            confidentialkey.write(secret_key)
            
    def load_secret_key(self, kname):
        with open(kname, 'rb') as confidentialkey:
            secret_key = confidentialkey.read()
        return secret_key

    def encrypt_file(self, secret_key, f_original, f_encrypted):
        f = Fernet(secret_key)
        with open(f_original, 'rb') as orgfile:
            original_file_data = orgfile.read()
        encrypted_data = f.encrypt(original_file_data)
        with open (f_encrypted, 'wb') as encfile:
            encfile.write(encrypted_data)

    def decrypt_file(self, secret_key, f_encrypted, f_decrypted):
        f = Fernet(secret_key)
        with open(f_encrypted, 'rb') as encfile:
            encrypted_file_data = encfile.read()
        decrypted_data = f.decrypt(encrypted_file_data)
        with open(f_decrypted, 'wb') as decfile:
            decfile.write(decrypted_data)

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = os.getcwd()+"/assets/", title = "Select a File to perform ciphering",filetypes = (("mp4", "*.mp4*"), ("all files","*.*")))
    return filename
window = Tk()
button_explore = Button(window,text = "Browse Files", command = browseFiles)
window.withdraw()     
# window.mainloop()

def newFileOrNot(dest_path):
    browsed_file = browseFiles() 
    if browsed_file=="":
        sys.exit("\nNo file selected from opened pop up window")
    else:   
        ext = "."+os.path.basename(browsed_file).split(".")[1] 
        file_Name = browsed_file
        print("Choosen file Path : ",file_Name)
        destination_path = dest_path
        print("\nChoose your option either y or n : \n\n (y) : If you want to create a new file after encryption - Enter y \n (n) : If you want to update existing original file as encrypted file - Enter n")

        while True:
            try:
                choosed_option = str(input("\nEnter your choosed option - ( y or n ) ? : "))
            except ValueError:
                print("\nSorry, I didn't understand that.")
                continue

            if choosed_option in ['y','n','Y','N']:
                if(choosed_option in ['y','Y']):
                    new_File=input("Enter the name of new File : ")
                    new_Filename = os.getcwd()+"/assets/"+destination_path+"/"+new_File+ext
                    print("Final File Destination Location",new_Filename)
                else:
                    new_Filename = file_Name
                    print("Final File Destination Location",new_Filename)

                break
            elif ch in ['q','Q']:
                print("\nSucessfully Exited from the program. \n\n-> Next time Enter either y or n values only - No other values are accepted kindly cooperate.")
                sys.exit("\n-> If you want to Encrypt or Decrypt your files please Execute the program again and dont repeat the same mistake, Thank You...")
            else:
                print("\nSorry, I didn't understand that. Please enter either y or n only, otherwise enter q or Q to exit from the program")
                continue
            print("Final File Destination Location",new_Filename)
    return file_Name, new_Filename


