# Напишете програма, която взима текст от потребителя използвайки input()
# и ограничава текста до 10 символа и добавя "..." накрая

text = input('Write something about you\n')
if len(text) < 10:
    print(text)
else:
    print(text[:10] + '...')
