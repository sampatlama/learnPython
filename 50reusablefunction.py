def emo_converter(msg):
    words = msg.split(' ')
    emoji_mapping = {
        ":(": "😔",
        ":)": "😍"
    }
    output = ''
    for word in words:
        output += emoji_mapping.get(word, word) + ' '
    return output
msg = input('> ')
result=emo_converter(msg)
print(result)
