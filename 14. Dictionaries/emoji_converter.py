emoji_mapping = {
    ":)": "😄",
    ":(": "😞",
    ";)": "😉",
    "<3": "❤️ "
}

msg = ''
while msg != 'quit' and msg != 'bye':
    msg = input('> ')
    words = msg.split()
    output = ''
    for word in words:
        output += emoji_mapping.get(word, word) + " "
    print(f'>> {output}')
