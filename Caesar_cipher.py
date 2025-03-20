alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print("Let's start....\n")

def encrypt(real_text,shift_num):
    cipher_text=""
    b=0
    for i in real_text:
        if i in alphabets:
            b=alphabets.index(i)
            cipher_text+=alphabets[(b+shift_num)%26]
    print(cipher_text)
def decrypt(cipher_text,shift_num):
    real_text=""
    b=0
    for i in cipher_text:
        if i in alphabets:
            b=alphabets.index(i)
            real_text+=alphabets[(b-shift_num)%26]
    print(real_text)

    

while True:
    print("----------------------------------------------------")
    print("Enter the your choice encrypt/1 or decrypt/0 !")
    choose=input()
    if choose=="encrypt" or choose=="1":
        print("Let's start the Encryption")
        real_text=input("Enter the real text\n")
        shift_num=int(input("Enter the Shift number:\n"))
        encrypt(real_text,shift_num)

    elif choose=="decrypt" or choose=="0":
        print("Let's start the Decryption")
        cipher_text=input("Enter the cipher text:\n")
        shift_num=int(input("Enter the Shift number:\n"))
        decrypt(cipher_text,shift_num)
    else:
        break