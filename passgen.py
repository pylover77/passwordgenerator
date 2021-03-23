import string
from random import *
import time

print  (""" 
            *PASSWORD GENERATOR*
            """)

def password_gen():

    characters = string.digits
    characters += string.punctuation
    characters += string.ascii_letters
    
    height_pass = int(input("input the lenght of password:"))
    passwd = ""

    for i in range(height_pass):
        passwd += choice(characters)
    print("GENERATING YOUR PASSWORD...")
    print(".")
    print("..")
    print("...")
    time.sleep(1.5)
    print(f'your password has been generated:\n PASSWORD: {passwd}')

password_gen()
