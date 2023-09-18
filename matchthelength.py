OriginalText = "MyPlainText"
KEY = "ABC"

print ("Here is the original Text")
print (OriginalText)

print("Here is the Key Repeated up to the lenth of the original text")
for position, letter in enumerate(OriginalText):
	x= KEY[position % len(KEY)]
	print(x,end='')

print()

Encrypted_Values = [int('0x0c',16), int('0x3b',16), int('0x13',16), int('0x2d',16), int('0x23',16), int('0x2a',16), int('0x2f',16), int('0x16',16), int('0x26',16), int('0x39',16), int('0x36',16)]

for position, letter in enumerate(OriginalText):
	Letter_In_Key = KEY[position % len(KEY)]
	encrypted_byte = ord(letter)^ord(Letter_In_Key)
	Encrypted_Values.append(encrypted_byte)

print ("Here is the encrypted Decimal")
print (Encrypted_Values)

print("Here is the encrypted Hex with the 0x preceding each value")
for i in Encrypted_Values:
	print(hex(i)+" ", end="")
print ()

print("Here is the encrypted Hex without the 0x preceding each value")
for i in Encrypted_Values:
	print(format(i, "x")+" ", end="")
