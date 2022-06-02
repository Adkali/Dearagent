# Python3.
# Made by Adkali with love.
# For beginner+.
# Have fun while trying.

import time
import random
from random import randint
import Greeting
Greeting.just_hello()
print("\nDear agent, our computers went through a DDos attack, and lots of credentials were exposed, but fortunately, we managed to respond\nquickly and block the incoming traffics that were getting into our network.\nnow please, identify yourself!\n")
time.sleep(2)
name = input("what is your name? ")
print("-" * 40)
print(f"{name}, just to be safe, Please log into your account again from security reasons only!")
print("-" * 40)
time.sleep(2)
tryme = "\x62\x6F\x6E\x64"
please = str(0 * 1)+str(1 - 1)
sumery = tryme + please + str(7)
useme = str(3 * 5)+str(round( 5 / 2))+str(1 + 1)+"007"

def mybeahint():
    call = "C:/\/Sou|d\Y0U\©heck\Th3\S0u®Ce\M@yB3?"
    print(call)
mybeahint()
def changeme():
    a = str(2 * 10)
    if a <= str(3 / 15):
        something = [ 82, 101, 109, 101, 109, 98, 101, 114, 59, 32, 42, 32, 98, 101, 102, 111, 114, 101, 32, 47 ]
        el_se = "".join(chr(i) for i in something)
        print(el_se)
        
changeme()

while True:
    user = input("username: ").lower()
    password = input("passs: ")
    if user == sumery:
        if password == useme:
            print(f"\nwelcome back, {user}")
            time.sleep(2)
            print("update your information now!")
            time.sleep(2)
            break
            
        elif password != useme:
            print("Wrong password!")
            
    else:
        print("wrong username!")
        
def nameme():
    a = input("what is your secret-name? ")
    b = input("what is your agent number please? ")
    
    print("_" * 39 + "\n")
    print(f"your agent number is {b}, and your secret name is {a}")
    print("_" * 39)
nameme()

time.sleep(2)
print("\nwant the flag? answer one last question and you will have it!")
time.sleep(2)

turns = 3
while turns > 0:
    guessme = random.randint(1, 6)
    tryme = input("Enter the secret number please: ")
    if tryme == str(guessme):
        print("you Won!")
        time.sleep(2)
        flag2u = "md51359z3ddf80sadfr"
        flag2me = "agk654" + flag2u
        fl = "\u004e\u006f\u0074\u0068\u0069\u006e\u0067"
        ag = "ButFlag"
        flag = [80, 114, 105, 122, 101, 123, 89, 111, 117, 95, 70, 111, 117, 110, 100, 95, 84, 104, 101, 95, 70, 108, 97, 103, 125 ]
        newflag = "".join(chr(i) for i in flag)
        print(fl + ag + " - MD5:", str(newflag))
        print(f"Hope you enjoyed the game, {name}.")
        break
        
    else:
        turns -=1
        print(f" you have {turns} turns left!")
