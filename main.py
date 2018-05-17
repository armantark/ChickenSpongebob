from random import choice

while True:
    text = input("Text: ")
    for i in range(len(text)):
        liststr = list(text)
        liststr[i] = choice([liststr[i].upper(), liststr[i].lower()])
        text = ''.join(liststr)
    print(text)
