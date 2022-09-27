from turtle import pos


alphabet_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
alphabet_2 = alphabet_1 + alphabet_1

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(shift_amount, text_input):
    new_cipher = ''
    for i in text_input:
        position = alphabet_2.index(i)
        new_position = position + shift_amount
        new_word = alphabet_2[new_position]
        new_cipher += new_word
    print(new_cipher)


encrypt(shift_amount=shift, text_input=text)
