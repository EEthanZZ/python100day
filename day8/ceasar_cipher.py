

alphabet_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
alphabet_2 = alphabet_1 + alphabet_1

game_on = True
while game_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def ceasar(dir, shift_amount, text_input):
        new_cipher = ''
        for i in text_input:
            position = alphabet_2.index(i)
            if dir == 'encode':
                new_position = position + shift_amount
            elif dir == 'decode':
                new_position = position - shift_amount
            new_word = alphabet_2[new_position]
            new_cipher += new_word
        print(f'you just {dir}, the new cipher is {new_cipher}')
    ceasar(direction, shift, text)
    x = input("continue?")
    if x == 'n':
        game_on = False
