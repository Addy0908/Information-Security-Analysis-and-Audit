Plain_Text = input("\n\nEnter your message: ").lower()
key = int(input("Enter the key for encrypting: "))

ascii = ord('a')

#Function for encrypting plain text to cipher text
def cipher(Plain_Text, key):
    CipherText = ""
    for i in range(len(Plain_Text)):
          CipherText += chr((ord(Plain_Text[i]) - ascii + key) % 26 + ascii)

    return CipherText 

CipherText =cipher(Plain_Text, key)
#output for cipher text
print(f"The encrypted cipher text is  : {cipher(Plain_Text, key)}")

#Function for converting into cipher text to plain text
def plaintext(Plain_Text, key):
    PlainText = ""
    for i in range(len(Plain_Text)):
      PlainText += chr((ord(Plain_Text[i])-ascii  + inverse(key)) % 26 + ascii)
    print("Inverse of the key is :",inverse(key))
    return PlainText

def inverse(i):
  for inverse in range(26):
    if(inverse + i)%26 == 0:
      return inverse


print("\n")
#text for plain text
print(f"Decrypting Plain Text : {plaintext(CipherText, key)}")