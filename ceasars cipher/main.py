from art import logo

print(logo)

def caesar_cipher(direction, text, shift):
    shifted_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            shifted_index = index + shift
            if direction == "encode":
                if shifted_index >= len(alphabet):
                    shifted_index = shifted_index - len(alphabet)
            else:
                if shifted_index < 0:
                    shifted_index = shifted_index + len(alphabet)
            shifted_text = shifted_text + alphabet[shifted_index]
        else:
            shifted_text = shifted_text + letter
    print(f"The {direction}d text is {shifted_text}")

isContinue = True

while isContinue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift >= len(alphabet):
        shift = shift % len(alphabet)
    caesar_cipher(direction, text, shift)
    restart = input("Type 'Y' if you wanna go again.\n").lower()
    if restart != "y":
        isContinue = False
