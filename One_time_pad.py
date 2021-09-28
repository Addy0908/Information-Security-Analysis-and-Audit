Plain_Text = input("Enter your message: ").lower()
Key = input("Enter the OTP :")

print(f"Message that you want to encrypt is : {Plain_Text}")
print(f"OTP for the message is : {Key}")

def replace_text(message):

  message = message.replace(" ", "")
  r = []
  for i in message:
    r.append(ord(i) - ord('a'))
  return r

def OTP(Plain_Text, key):
  plaintext = replace_text(Plain_Text)
  Key = replace_text(key)
  cMatrix = []
  for i in range (len(plaintext)):
    cMatrix.append((plaintext[i]+Key[i%len(Key)])%26)
  cText = ""
  for i in cMatrix:
    cText += chr(i+ord('A'))
  return cText

cipherText = OTP(Plain_Text,Key)
print(f"The  encrypted cipher message generated is :{cipherText}")

def addInv(num):
  for i in range(26):
    if (i+num)%26 == 0:
      return i

def Regenating_plain_text(cipherText, key):
  cText = replace_text(cipherText)
  Key = replace_text(key)
  pMatrix = []

  for i in range( len(cText)):
    pMatrix.append((cText[i]+ addInv(Key[i%len(Key)]))%26)
  plaintext =""
  for i in pMatrix:
    plaintext += chr(i+ord('A'))
  return plaintext


Generated_plain_text = Regenating_plain_text(cipherText,Key)
print(f"The generated plain message is :{Generated_plain_text}")