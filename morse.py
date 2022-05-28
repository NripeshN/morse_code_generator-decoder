MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    '"': '.-..-.',
    '@': '.--.-.',
    ':': '---...',
    '=': '-...-',
    '+': '.-.-.',
    '_': '..--.-',
    '\'': '.----.',
    '!': '-.-.--',
    '$': '...-..-',
    '&': '.-...',
    ' ': '/'
}


def to_text(morse):
    text = ''
    for char in morse.split(' '):
        for key, value in MORSE_CODE.items():
            if value == char:
                text += key
    return text


def to_morse(text):
    morse = ''
    for char in text:
        for key, value in MORSE_CODE.items():
            if key == char:
                morse += value + ' '
    return morse


def main():
    print('Morse Code Converter')
    print('1. Convert text to morse(Enter text in capital letters)')
    print('2. Convert morse to text')
    choice = input('Enter your choice: ')
    if choice == '1':
        text = input('Enter text to convert: ')
        morse = to_morse(text)
        print(morse)
    elif choice == '2':
        morse = input('Enter morse to convert: ')
        text = to_text(morse)
        print(text)
    else:
        print('Invalid choice')


main()
