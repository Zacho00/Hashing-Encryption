def caesar(message, randnum):
    breakdown = []
    encryption = []
    for letter in message:
        breakdown.append(letter)
    for i in breakdown:
        encryption.append(ord(i) + randnum)
    uncaesar(encryption, randnum)

def uncaesar(encryption, randnum):
    unscramble = []
    noKey = []
    count = 0
    letter = ''
    decryption = ''
    for i in encryption:
        noKey.append(chr(i))
    for i in encryption:
        unscramble.append(chr(i - randnum))
    for i in unscramble:
        letter = unscramble[count]
        decryption = decryption + letter
        count += 1
    print("---Report---" \
    "\nYour Message:", message,
    '\nYour Encryption:', encryption,
    '\nYour Decryption without a key:', noKey,
    '\nYour Decryption:', decryption,
    '\n---End of Report---')


import random
message = input("What would you like encrypted? ")
randnum = random.randint(2, 14)

caesar(message, randnum)