# C:/PycharmProjects/untitled1/morse_translation.py

dic = {
    '.-':'a', '-...':'b', '-..':'d', '.':'e', '..-.':'f',
    '--.':'g', '....':'h', '..':'i', '-.-':'k', '.-..':'l',
    '--':'m', '-.':'n', '---':'o','.--.':'p', '--.-':'q', '.-.':'r',
    '...':'s', '-':'t', '..-':'u', '...-':'v', '.--w':'f','-..-':'x',
    '-.--':'y','--..':'z'


}

def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)

print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))
