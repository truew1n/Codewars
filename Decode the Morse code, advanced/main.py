def decode_bits(bits):
    bits = bits.strip('0')
    rate = min([len(s) for s in bits.split('1') + bits.split('0') if s])
    return bits.replace('111' * rate, '-').replace('1' * rate, '.').replace('0000000' * rate, '   ').replace('000' * rate, ' ').replace('0' * rate, '')


def decode_morse(morse_code):
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', '!':'-.-.--',
                    'SOS': '...---...'}
    
    result = ""
    
    words = morse_code.split("   ")
    
    if '' in words:
        for x in range(words.count('')):
            words.pop(words.index(''))
    for word in words:
        for x in word.split(" "):
            for char, value in MORSE_CODE_DICT.items():
                if x == value:
                    result += char
                else:
                    pass
        result+= " "
    return result[:-1]
