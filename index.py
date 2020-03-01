import time
import re

config = open("config.txt","r")
configswithn = []
configs = []
output = []

for line in config:
    configswithn.append(line)
for each in configswithn:
    x = each.split("\n")
    configs.append(x[0])

hr = "-----------------------------------------------"
print(hr)
decision = int(input("Would you like to\n \n1) Encrypt Message\nor\n2) Decrypt Message\n \n[Reply with '1' or '2']\n-----------------------------------------------\n"))
while True:
    if decision == 1:
        print(hr)
        print("You chose ENCRYPT!")
        print(hr)
        message = input("What message would you like to encrypt? [only input numbers, letters, and spaces]\n-----------------------------------------------\nYour Input: ")
        character = re.findall('.', message)
        for x in character:
            for a in configs:
                splitted = a.split(": ")
                if x == splitted[0]:
                    output.append(splitted[1])
        outputmessage = ''.join(output)
        print(f"Encrypted Message: {outputmessage}")
        break
    if decision == 2:
        print(hr)
        print("You chose DECRYPT!")
        print(hr)
        message = input("What message would you like to decrypt? [only input a message that was previously encrypted with this software]\n-----------------------------------------------\nYour Input: ")
        character = re.findall('.', message)
        for x in character:
            for a in configs:
                splitted = a.split(": ")
                if x == splitted[1]:
                    output.append(splitted[0])
        outputmessage = ''.join(output)
        print(f"Decrypted Message: {outputmessage}")
        break
    if decision != 1 or 2:
        print(hr)
        decision = int(input("Error! Please input '1' or '2'!\n-----------------------------------------------\n"))
    time.sleep(.1)